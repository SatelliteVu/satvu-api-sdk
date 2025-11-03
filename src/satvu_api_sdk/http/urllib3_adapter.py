"""Urllib3 HTTP adapter."""

import json as json_lib
from collections.abc import Callable
from typing import Any, cast
from urllib.parse import urlencode, urljoin

try:
    import urllib3
except ImportError:
    raise ImportError(
        "urllib3 is required to use Urllib3Adapter. "
        'Install it with: pip install "satvu-api-sdk[http-urllib3]"'
    )

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


class Urllib3Response:
    """Wrapper for urllib3 HTTPResponse to conform to HttpResponse protocol."""

    def __init__(self, response: urllib3.BaseHTTPResponse):
        self._response = response
        self._body: bytes | None = None

    @property
    def status_code(self) -> int:
        return self._response.status

    @property
    def headers(self) -> dict[str, str]:
        return dict(self._response.headers.items())

    @property
    def body(self) -> bytes:
        if self._body is None:
            self._body = self._response.data
        # Type checker doesn't know _body is not None after assignment
        assert self._body is not None  # nosec B101
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


class Urllib3Adapter:
    """
    HTTP client adapter using urllib3 library.

    Provides lower-level HTTP functionality with connection pooling
    and more control over request/response handling.
    """

    def __init__(
        self,
        base_url: str | None = None,
        pool_manager: urllib3.PoolManager | None = None,
        get_token: Callable[[], str] | None = None,
    ):
        """
        Initialize the urllib3 adapter.

        Args:
            base_url: Optional base URL for all requests. Relative URLs will be joined to this.
            pool_manager: Optional pre-configured urllib3.PoolManager instance.
                         If not provided, a new one will be created.
            get_token: Optional callback to get the current access token. Will be called
                      before each request to support token refresh.
        """
        self.base_url = base_url.rstrip("/") if base_url else ""
        self.get_token = get_token

        if pool_manager is not None:
            self.pool_manager = pool_manager
            self._owns_pool = False
        else:
            self.pool_manager = urllib3.PoolManager()
            self._owns_pool = True

    def __del__(self):
        """Clean up pool manager if we own it."""
        if self._owns_pool and hasattr(self, "pool_manager"):
            self.pool_manager.clear()

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
        """Make an HTTP request using urllib3."""
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
        body_data: bytes | str | None = None
        if json is not None:
            body_data = json_lib.dumps(json)
            req_headers["Content-Type"] = "application/json"
        elif data is not None:
            body_data = urlencode(data)
            req_headers["Content-Type"] = "application/x-www-form-urlencoded"

        # Make request
        try:
            response = self.pool_manager.request(
                method=method,
                url=full_url,
                headers=req_headers,
                body=body_data,
                timeout=timeout,
                redirect=follow_redirects,
            )

            response_wrapper = Urllib3Response(response)

            # Check for error status codes
            if 400 <= response.status < 500:
                return Err(
                    ClientError(
                        message=f"Client error: {response.status}",
                        status_code=response.status,
                        url=full_url,
                        response_body=response.data,
                        response_headers=dict(response.headers.items()),
                    )
                )
            elif 500 <= response.status < 600:
                return Err(
                    ServerError(
                        message=f"Server error: {response.status}",
                        status_code=response.status,
                        url=full_url,
                        response_body=response.data,
                        response_headers=dict(response.headers.items()),
                    )
                )

            return Ok(cast(HttpResponse, response_wrapper))

        except urllib3.exceptions.NewConnectionError as e:
            return Err(
                NetworkError(
                    message=f"Failed to establish connection: {e}",
                    url=full_url,
                    original_error=e,
                )
            )

        except urllib3.exceptions.ConnectTimeoutError as e:
            return Err(
                ConnectionTimeoutError(
                    message=f"Connection timeout after {timeout} seconds",
                    url=full_url,
                    timeout=timeout,
                    original_error=e,
                )
            )

        except urllib3.exceptions.ReadTimeoutError as e:
            return Err(
                ReadTimeoutError(
                    message=f"Read timeout after {timeout} seconds",
                    url=full_url,
                    timeout=timeout,
                    original_error=e,
                )
            )

        except urllib3.exceptions.TimeoutError as e:
            # Generic timeout
            return Err(
                ReadTimeoutError(
                    message=f"Request timeout after {timeout} seconds",
                    url=full_url,
                    timeout=timeout,
                    original_error=e,
                )
            )

        except urllib3.exceptions.ProxyError as e:
            return Err(
                ProxyError(
                    message=f"Proxy error: {e}",
                    url=full_url,
                    original_error=e,
                )
            )

        except urllib3.exceptions.SSLError as e:
            return Err(
                SSLError(
                    message=f"SSL/TLS error: {e}",
                    url=full_url,
                    original_error=e,
                )
            )

        except urllib3.exceptions.MaxRetryError as e:
            # MaxRetryError can wrap various errors
            reason = str(e.reason) if e.reason else str(e)

            if "timed out" in reason.lower():
                return Err(
                    ReadTimeoutError(
                        message=f"Request timed out: {reason}",
                        url=full_url,
                        timeout=timeout,
                        original_error=e,
                    )
                )

            return Err(
                NetworkError(
                    message=f"Max retries exceeded: {reason}",
                    url=full_url,
                    original_error=e,
                )
            )

        except urllib3.exceptions.HTTPError as e:
            # Generic urllib3 HTTP error (base class)
            return Err(
                NetworkError(
                    message=f"HTTP error: {e}",
                    url=full_url,
                    original_error=e,
                )
            )
