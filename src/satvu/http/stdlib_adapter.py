"""Standard library HTTP adapter using urllib."""

import json as json_lib
import socket
import warnings
from collections.abc import Callable, Iterator
from http.client import HTTPResponse as StdlibHTTPResponse
from typing import Any, cast
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen

from satvu.http.errors import (
    ClientError,
    ConnectionTimeoutError,
    JsonDecodeError,
    NetworkError,
    ProxyError,
    ReadTimeoutError,
    ServerError,
    SSLError,
    TextDecodeError,
)
from satvu.http.protocol import HttpMethod, HttpResponse
from satvu.result import Err, Ok, Result, is_err


class StdlibResponse:
    """Wrapper for urllib HTTP response to conform to HttpResponse protocol."""

    def __init__(self, response: StdlibHTTPResponse | HTTPError, url: str):
        self._response = response
        self._url = url
        self._body: bytes | None = None
        self._consumed = False  # Track if response stream has been consumed

    @property
    def status_code(self) -> int:
        """HTTP status code of the response, or -1 if unavailable."""
        return self._response.status or -1

    @property
    def headers(self) -> dict[str, str]:
        return dict(self._response.headers.items())

    @property
    def body(self) -> bytes:
        if self._body is None:
            self._body = self._response.read()
        return self._body

    def iter_bytes(self, chunk_size: int = 8192) -> Iterator[bytes]:
        """
        Stream response body in chunks without loading it all into memory.

        This is the key method for handling large file downloads efficiently.
        It reads the response incrementally using the underlying urllib response object.

        Args:
            chunk_size: Number of bytes to read per chunk (default: 8KB)

        Yields:
            Chunks of bytes from the response body

        Raises:
            RuntimeError: If response stream has already been consumed by a previous
                         call to iter_bytes()

        Implementation Notes:
            - If .body property was already called, the cached body is yielded in chunks
            - Otherwise, reads directly from the urllib response object in a streaming fashion
            - Marks response as consumed after first streaming call to prevent double consumption
        """
        if self._consumed is True:
            raise RuntimeError(
                "Response body has already been consumed via iter_bytes(). "
                "Each response can only be streamed once."
            )

        # Case 1: Body was already loaded via .body property
        # In this case, we yield the cached body in chunks (still useful for uniform API)
        if self._body is not None:
            for i in range(0, len(self._body), chunk_size):
                yield self._body[i : i + chunk_size]
            return

        # Case 2: Stream directly from the underlying response (memory-efficient)
        # This is the main use case for large file downloads
        self._consumed = True
        while True:
            try:
                chunk = self._response.read(chunk_size)
            except TypeError:
                # Some mock libraries (e.g., pook) don't support read(size) argument
                # Fall back to reading entire body and yielding it in chunks
                remaining_body = self._response.read()
                if remaining_body:
                    for i in range(0, len(remaining_body), chunk_size):
                        yield remaining_body[i : i + chunk_size]
                break
            if not chunk:
                # End of response reached
                break
            yield chunk

    @property
    def text(self) -> Result[str, TextDecodeError]:
        """Decode response body as text with error handling."""
        try:
            return Ok(self.body.decode("utf-8"))
        except UnicodeDecodeError as e:
            return Err(
                TextDecodeError(
                    message=f"Failed to decode response body as UTF-8: {e}",
                    encoding="utf-8",
                    original_error=e,
                )
            )

    def json(self) -> Result[Any, JsonDecodeError | TextDecodeError]:
        """Parse response body as JSON with error handling."""
        text_result = self.text
        if is_err(text_result):
            # If we can't decode text, wrap it in JsonDecodeError
            text_err = text_result.error()
            return Err(
                JsonDecodeError(
                    message=f"Cannot parse JSON: {text_err.message}",
                    body=None,
                    original_error=text_err.original_error,
                )
            )

        text_value = text_result.unwrap()
        try:
            return Ok(json_lib.loads(text_value))
        except json_lib.JSONDecodeError as e:
            return Err(
                JsonDecodeError(
                    message=f"Failed to parse JSON: {e}",
                    body=text_value,
                    original_error=e,
                )
            )


class StdlibAdapter:
    """
    HTTP client adapter using Python's standard library (urllib).

    Zero external dependencies. Suitable for minimal installations.
    """

    def __init__(
        self, base_url: str | None = None, get_token: Callable[[], str] | None = None
    ):
        """
        Initialize the stdlib adapter.

        Args:
            base_url: Optional base URL for all requests. Relative URLs will be joined to this.
            get_token: Optional callback to get the current access token. Will be called
                      before each request to support token refresh.
        """
        self.base_url = base_url.rstrip("/") if base_url else ""
        self.get_token = get_token

    def request(
        self,
        method: HttpMethod,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | list | None = None,
        data: dict[str, str] | None = None,
        timeout: float = 5.0,
        follow_redirects: bool = False,
    ) -> Result[
        HttpResponse,
        ClientError
        | ServerError
        | NetworkError
        | ConnectionTimeoutError
        | ReadTimeoutError
        | SSLError
        | ProxyError,
    ]:
        """Make an HTTP request using urllib."""
        # Warn if follow_redirects is False (urllib always follows redirects)
        if not follow_redirects:
            warnings.warn(
                "StdlibAdapter does not support follow_redirects=False. "
                "Redirects will be followed automatically by urllib.",
                UserWarning,
                stacklevel=2,
            )

        # Build full URL
        if self.base_url and not url.startswith(("http://", "https://")):
            full_url = urljoin(self.base_url + "/", url.lstrip("/"))
        else:
            full_url = url

        # Add query parameters
        if params:
            # Filter out None values
            filtered_params = {k: v for k, v in params.items() if v is not None}
            if filtered_params:
                query_string = urlencode(filtered_params, doseq=True)
                separator = "&" if "?" in full_url else "?"
                full_url = f"{full_url}{separator}{query_string}"

        # Prepare headers with auth token if get_token is available
        req_headers = headers.copy() if headers else {}
        if self.get_token:
            token = self.get_token()
            req_headers["Authorization"] = f"Bearer {token}"

        # Prepare body
        body_data: bytes | None = None
        if json is not None:
            body_data = json_lib.dumps(json).encode("utf-8")
            req_headers["Content-Type"] = "application/json"
        elif data is not None:
            body_data = urlencode(data).encode("utf-8")
            req_headers["Content-Type"] = "application/x-www-form-urlencoded"

        # Create request
        request = Request(
            full_url,
            data=body_data,
            headers=req_headers,
            method=method,
        )

        # Make request
        try:
            response = urlopen(request, timeout=timeout)
            response_wrapper = StdlibResponse(response, full_url)

            # Check for error status codes
            if 400 <= response_wrapper.status_code < 500:
                return Err(
                    ClientError(
                        message=f"Client error: {response_wrapper.status_code}",
                        status_code=response_wrapper.status_code,
                        url=full_url,
                        response_body=response_wrapper.body,
                        response_headers=response_wrapper.headers,
                    )
                )
            elif 500 <= response_wrapper.status_code < 600:
                return Err(
                    ServerError(
                        message=f"Server error: {response_wrapper.status_code}",
                        status_code=response_wrapper.status_code,
                        url=full_url,
                        response_body=response_wrapper.body,
                        response_headers=response_wrapper.headers,
                    )
                )

            return Ok(cast(HttpResponse, response_wrapper))

        except HTTPError as e:
            # HTTPError has response data and status code
            response_wrapper = StdlibResponse(e, full_url)
            status_code = response_wrapper.status_code

            if 400 <= status_code < 500:
                return Err(
                    ClientError(
                        message=f"Client error: {status_code}",
                        status_code=status_code,
                        url=full_url,
                        response_body=response_wrapper.body,
                        response_headers=response_wrapper.headers,
                    )
                )
            elif 500 <= status_code < 600:
                return Err(
                    ServerError(
                        message=f"Server error: {status_code}",
                        status_code=status_code,
                        url=full_url,
                        response_body=response_wrapper.body,
                        response_headers=response_wrapper.headers,
                    )
                )
            else:
                # Shouldn't happen, but treat as network error
                return Err(
                    NetworkError(
                        message=f"Unexpected HTTP error: {e}",
                        url=full_url,
                        original_error=e,
                    )
                )

        except TimeoutError as e:
            # Socket timeout - could be connection or read timeout
            # urllib doesn't distinguish, so we'll call it read timeout
            return Err(
                ReadTimeoutError(
                    message=f"Request timed out after {timeout} seconds",
                    url=full_url,
                    timeout=timeout,
                    original_error=e,
                )
            )

        except URLError as e:
            # URLError wraps various errors
            reason = str(e.reason)

            # Check for SSL errors
            if "SSL" in reason or "CERTIFICATE" in reason.upper():
                return Err(
                    SSLError(
                        message=f"SSL/TLS error: {reason}",
                        url=full_url,
                        original_error=e,
                    )
                )

            # Check for proxy errors
            if "proxy" in reason.lower():
                return Err(
                    ProxyError(
                        message=f"Proxy error: {reason}",
                        url=full_url,
                        original_error=e,
                    )
                )

            # Check for timeout in the reason (sometimes wrapped in URLError)
            if isinstance(e.reason, socket.timeout):
                return Err(
                    ReadTimeoutError(
                        message=f"Request timed out after {timeout} seconds",
                        url=full_url,
                        timeout=timeout,
                        original_error=e,
                    )
                )

            # Generic network error
            return Err(
                NetworkError(
                    message=f"Network error: {reason}",
                    url=full_url,
                    original_error=e,
                )
            )

        except OSError as e:
            # Catch-all for other OS-level errors (connection refused, etc.)
            return Err(
                NetworkError(
                    message=f"OS error during request: {e}",
                    url=full_url,
                    original_error=e,
                )
            )
