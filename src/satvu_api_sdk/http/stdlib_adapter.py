"""Standard library HTTP adapter using urllib."""

import json as json_lib
import socket
import warnings
from collections.abc import Callable
from http.client import HTTPResponse as StdlibHTTPResponse
from typing import Any, cast
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen

from satvu_api_sdk.http.errors import (
    ClientError,
    ConnectionTimeoutError,
    JsonDecodeError,
    NetworkError,
    ProxyError,
    ReadTimeoutError,
    SSLError,
    ServerError,
    TextDecodeError,
)
from satvu_api_sdk.http.protocol import HttpMethod, HttpResponse
from satvu_api_sdk.result import Err, Ok, Result, is_err


class StdlibResponse:
    """Wrapper for urllib HTTP response to conform to HttpResponse protocol."""

    def __init__(self, response: StdlibHTTPResponse | HTTPError, url: str):
        self._response = response
        self._url = url
        self._body: bytes | None = None

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

        except socket.timeout as e:
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
