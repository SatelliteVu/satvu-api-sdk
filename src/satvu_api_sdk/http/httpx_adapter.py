"""HTTPX HTTP adapter."""

import json as json_lib
from collections.abc import Callable
from typing import Any, cast

try:
    import httpx
except ImportError:
    raise ImportError(
        "httpx is required to use HTTPXAdapter. "
        'Install it with: pip install "satvu-api-sdk[http-httpx]"'
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


class HttpxResponse:
    """Wrapper for httpx Response to conform to HttpResponse protocol."""

    def __init__(self, response: httpx.Response):
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
        # httpx.Response.json() internally calls .text then json.loads
        # We'll replicate this to have control over error types
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


class HttpxAdapter:
    """
    HTTP client adapter using httpx library.

    Provides advanced features like connection pooling, HTTP/2 support,
    and better performance than stdlib.
    """

    def __init__(
        self,
        base_url: str | None = None,
        client: httpx.Client | None = None,
        get_token: Callable[[], str] | None = None,
    ):
        """
        Initialize the httpx adapter.

        Args:
            base_url: Optional base URL for all requests. Relative URLs will be joined to this.
            client: Optional pre-configured httpx.Client instance. If not provided,
                   a new client will be created.
            get_token: Optional callback to get the current access token. Will be called
                      before each request to support token refresh.
        """
        self.get_token = get_token
        if client is not None:
            self.client = client
            self._owns_client = False
        else:
            self.client = httpx.Client(base_url=base_url or "")
            self._owns_client = True

    def __del__(self):
        """Clean up client if we own it."""
        if self._owns_client and hasattr(self, "client"):
            self.client.close()

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
        """Make an HTTP request using httpx."""
        # Prepare headers with auth token if get_token is available
        req_headers = headers.copy() if headers else {}
        if self.get_token:
            token = self.get_token()
            req_headers["Authorization"] = f"Bearer {token}"

        # Filter out None values from params
        if params:
            params = {k: v for k, v in params.items() if v is not None}

        try:
            response = self.client.request(
                method=method,
                url=url,
                headers=req_headers,
                params=params,
                json=json,
                data=data,
                timeout=timeout,
                follow_redirects=follow_redirects,
            )

            response_wrapper = HttpxResponse(response)

            # Check for error status codes
            if 400 <= response.status_code < 500:
                return Err(
                    ClientError(
                        message=f"Client error: {response.status_code}",
                        status_code=response.status_code,
                        url=str(response.url),
                        response_body=response.content,
                        response_headers=dict(response.headers.items()),
                    )
                )
            elif 500 <= response.status_code < 600:
                return Err(
                    ServerError(
                        message=f"Server error: {response.status_code}",
                        status_code=response.status_code,
                        url=str(response.url),
                        response_body=response.content,
                        response_headers=dict(response.headers.items()),
                    )
                )

            return Ok(cast(HttpResponse, response_wrapper))

        except httpx.ConnectTimeout as e:
            return Err(
                ConnectionTimeoutError(
                    message=f"Connection timeout after {timeout} seconds",
                    url=url,
                    timeout=timeout,
                    original_error=e,
                )
            )

        except httpx.ReadTimeout as e:
            return Err(
                ReadTimeoutError(
                    message=f"Read timeout after {timeout} seconds",
                    url=url,
                    timeout=timeout,
                    original_error=e,
                )
            )

        except httpx.TimeoutException as e:
            # Generic timeout (could be connect, read, write, or pool)
            return Err(
                ReadTimeoutError(
                    message=f"Request timeout after {timeout} seconds",
                    url=url,
                    timeout=timeout,
                    original_error=e,
                )
            )

        except httpx.ProxyError as e:
            return Err(
                ProxyError(
                    message=f"Proxy error: {e}",
                    url=url,
                    original_error=e,
                )
            )

        except httpx.ConnectError as e:
            # SSL/TLS errors are a type of ConnectError in httpx
            if "SSL" in str(e) or "TLS" in str(e) or "certificate" in str(e).lower():
                return Err(
                    SSLError(
                        message=f"SSL/TLS error: {e}",
                        url=url,
                        original_error=e,
                    )
                )
            return Err(
                NetworkError(
                    message=f"Connection error: {e}",
                    url=url,
                    original_error=e,
                )
            )

        except httpx.NetworkError as e:
            # Generic network error (base class for connect, timeout, etc.)
            return Err(
                NetworkError(
                    message=f"Network error: {e}",
                    url=url,
                    original_error=e,
                )
            )

        except httpx.HTTPError as e:
            # Catch-all for any other httpx HTTP errors
            return Err(
                NetworkError(
                    message=f"HTTP error: {e}",
                    url=url,
                    original_error=e,
                )
            )
