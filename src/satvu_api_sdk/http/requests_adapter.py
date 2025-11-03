"""Requests HTTP adapter."""

import json as json_lib
from collections.abc import Callable
from typing import Any, cast

try:
    import requests
except ImportError:
    raise ImportError(
        "requests is required to use RequestsAdapter. "
        'Install it with: pip install "satvu-api-sdk[http-requests]"'
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


class RequestsResponse:
    """Wrapper for requests Response to conform to HttpResponse protocol."""

    def __init__(self, response: requests.Response):
        self._response = response

    @property
    def status_code(self) -> int:
        return self._response.status_code

    @property
    def headers(self) -> dict[str, str]:
        return dict(self._response.headers.items())

    @property
    def body(self) -> bytes:
        return self._response.content

    @property
    def text(self) -> Result[str, TextDecodeError]:
        """Decode response body as text with error handling."""
        try:
            return Ok(self._response.text)
        except UnicodeDecodeError as e:
            return Err(
                TextDecodeError(
                    message=f"Failed to decode response body: {e}",
                    encoding=self._response.encoding,
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


class RequestsAdapter:
    """
    HTTP client adapter using requests library.

    The most popular HTTP library in Python, known for its simple
    and elegant API. Widely used and well-documented.
    """

    def __init__(
        self,
        base_url: str | None = None,
        session: requests.Session | None = None,
        get_token: Callable[[], str] | None = None,
    ):
        """
        Initialize the requests adapter.

        Args:
            base_url: Optional base URL for all requests. Relative URLs will be joined to this.
            session: Optional pre-configured requests.Session instance. If not provided,
                    a new session will be created.
            get_token: Optional callback to get the current access token. Will be called
                      before each request to support token refresh.
        """
        self.base_url = base_url.rstrip("/") if base_url else ""
        self.get_token = get_token

        if session is not None:
            self.session = session
            self._owns_session = False
        else:
            self.session = requests.Session()
            self._owns_session = True

    def __del__(self):
        """Clean up session if we own it."""
        if self._owns_session and hasattr(self, "session"):
            self.session.close()

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
        """Make an HTTP request using requests."""
        # Build full URL
        if self.base_url and not url.startswith(("http://", "https://")):
            full_url = f"{self.base_url}/{url.lstrip('/')}"
        else:
            full_url = url

        # Prepare headers with auth token if get_token is available
        req_headers = headers.copy() if headers else {}
        if self.get_token:
            token = self.get_token()
            req_headers["Authorization"] = f"Bearer {token}"

        # Filter out None values from params
        if params:
            params = {k: v for k, v in params.items() if v is not None}

        # Make request
        try:
            response = self.session.request(
                method=method,
                url=full_url,
                headers=req_headers,
                params=params,
                json=json,
                data=data,
                timeout=timeout,
                allow_redirects=follow_redirects,
            )

            response_wrapper = RequestsResponse(response)

            # Check for error status codes
            if 400 <= response.status_code < 500:
                return Err(
                    ClientError(
                        message=f"Client error: {response.status_code}",
                        status_code=response.status_code,
                        url=response.url,
                        response_body=response.content,
                        response_headers=dict(response.headers.items()),
                    )
                )
            elif 500 <= response.status_code < 600:
                return Err(
                    ServerError(
                        message=f"Server error: {response.status_code}",
                        status_code=response.status_code,
                        url=response.url,
                        response_body=response.content,
                        response_headers=dict(response.headers.items()),
                    )
                )

            return Ok(cast(HttpResponse, response_wrapper))

        except requests.exceptions.ConnectTimeout as e:
            return Err(
                ConnectionTimeoutError(
                    message=f"Connection timeout after {timeout} seconds",
                    url=full_url,
                    timeout=timeout,
                    original_error=e,
                )
            )

        except requests.exceptions.ReadTimeout as e:
            return Err(
                ReadTimeoutError(
                    message=f"Read timeout after {timeout} seconds",
                    url=full_url,
                    timeout=timeout,
                    original_error=e,
                )
            )

        except requests.exceptions.Timeout as e:
            # Generic timeout (could be connect or read)
            return Err(
                ReadTimeoutError(
                    message=f"Request timeout after {timeout} seconds",
                    url=full_url,
                    timeout=timeout,
                    original_error=e,
                )
            )

        except requests.exceptions.ProxyError as e:
            return Err(
                ProxyError(
                    message=f"Proxy error: {e}",
                    url=full_url,
                    original_error=e,
                )
            )

        except requests.exceptions.SSLError as e:
            return Err(
                SSLError(
                    message=f"SSL/TLS error: {e}",
                    url=full_url,
                    original_error=e,
                )
            )

        except requests.exceptions.ConnectionError as e:
            return Err(
                NetworkError(
                    message=f"Connection error: {e}",
                    url=full_url,
                    original_error=e,
                )
            )

        except requests.exceptions.RequestException as e:
            # Generic requests exception (base class)
            return Err(
                NetworkError(
                    message=f"Request error: {e}",
                    url=full_url,
                    original_error=e,
                )
            )
