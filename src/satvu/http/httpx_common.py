"""
Shared implementation for the httpx and httpx2 adapters.
"""

import json as json_lib
from collections.abc import Callable, Iterator, Mapping
from typing import Any, ClassVar, Protocol, cast

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

HttpxTransportError = (
    NetworkError | ConnectionTimeoutError | ReadTimeoutError | SSLError | ProxyError
)
HttpxRequestError = ClientError | ServerError | HttpxTransportError


class HttpxLikeResponse(Protocol):
    """The subset of ``httpx.Response`` the adapters rely on."""

    @property
    def status_code(self) -> int: ...

    @property
    def headers(self) -> Mapping[str, str]: ...

    @property
    def content(self) -> bytes: ...

    @property
    def encoding(self) -> str | None: ...

    @property
    def text(self) -> str: ...

    @property
    def url(self) -> Any: ...

    def iter_bytes(self, chunk_size: int | None = ...) -> Iterator[bytes]: ...


class HttpxLikeModule(Protocol):
    """
    The surface an httpx-compatible module must expose to back an adapter.
    """

    @property
    def Client(self) -> type[Any]: ...

    @property
    def HTTPError(self) -> type[Exception]: ...

    @property
    def ConnectTimeout(self) -> type[Exception]: ...

    @property
    def ReadTimeout(self) -> type[Exception]: ...

    @property
    def TimeoutException(self) -> type[Exception]: ...

    @property
    def ProxyError(self) -> type[Exception]: ...

    @property
    def ConnectError(self) -> type[Exception]: ...

    @property
    def NetworkError(self) -> type[Exception]: ...


class HttpxResponse:
    """Wrapper for an httpx/httpx2 Response to conform to HttpResponse protocol."""

    def __init__(self, response: HttpxLikeResponse):
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

    def iter_bytes(self, chunk_size: int = 8192) -> Iterator[bytes]:
        """
        Stream response body in chunks without loading it all into memory.

        httpx has excellent native streaming support via iter_bytes(), which we
        leverage directly. httpx handles the complexity of chunked transfer encoding,
        compression, and other HTTP details automatically.

        Args:
            chunk_size: Number of bytes to read per chunk (default: 8KB)

        Yields:
            Chunks of bytes from the response body

        Note:
            httpx's iter_bytes() can only be called once. If the response content
            has already been accessed via .content or .text, this will yield the
            cached content in chunks (httpx handles this automatically).

        Implementation:
            We delegate directly to httpx.Response.iter_bytes() which provides
            efficient streaming with proper connection management.
        """
        # httpx.Response.iter_bytes() is a generator that yields chunks
        # It handles all the complexity: chunked encoding, compression, etc.
        return self._response.iter_bytes(chunk_size=chunk_size)

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


def status_error(response: HttpxLikeResponse) -> ClientError | ServerError | None:
    """Map a 4xx/5xx response onto an error, or None for any other status."""
    if 400 <= response.status_code < 500:
        return ClientError(
            message=f"Client error: {response.status_code}",
            status_code=response.status_code,
            url=str(response.url),
            response_body=response.content,
            response_headers=dict(response.headers.items()),
        )

    if 500 <= response.status_code < 600:
        return ServerError(
            message=f"Server error: {response.status_code}",
            status_code=response.status_code,
            url=str(response.url),
            response_body=response.content,
            response_headers=dict(response.headers.items()),
        )

    return None


def translate_transport_error(
    module: HttpxLikeModule, exc: Exception, url: str, timeout: float
) -> HttpxTransportError:
    """
    Map an httpx/httpx2 HTTPError onto the SDK's error hierarchy.

    Order is load-bearing: ConnectError subclasses NetworkError, ConnectTimeout and
    ReadTimeout subclass TimeoutException, and ProxyError is a sibling of NetworkError
    rather than a child. Checking a base class before its subclasses silently
    reclassifies errors.
    """
    timeout_error = _translate_timeout(module, exc, url, timeout)
    if timeout_error is not None:
        return timeout_error

    return _translate_network(module, exc, url)


def _translate_timeout(
    module: HttpxLikeModule, exc: Exception, url: str, timeout: float
) -> ConnectionTimeoutError | ReadTimeoutError | None:
    if isinstance(exc, module.ConnectTimeout):
        return ConnectionTimeoutError(
            message=f"Connection timeout after {timeout} seconds",
            url=url,
            timeout=timeout,
            original_error=exc,
        )

    if isinstance(exc, module.ReadTimeout):
        return ReadTimeoutError(
            message=f"Read timeout after {timeout} seconds",
            url=url,
            timeout=timeout,
            original_error=exc,
        )

    if isinstance(exc, module.TimeoutException):
        # Generic timeout (could be connect, read, write, or pool)
        return ReadTimeoutError(
            message=f"Request timeout after {timeout} seconds",
            url=url,
            timeout=timeout,
            original_error=exc,
        )

    return None


def _translate_network(
    module: HttpxLikeModule, exc: Exception, url: str
) -> NetworkError | SSLError | ProxyError:
    if isinstance(exc, module.ProxyError):
        return ProxyError(message=f"Proxy error: {exc}", url=url, original_error=exc)

    if isinstance(exc, module.ConnectError):
        # SSL/TLS errors are a type of ConnectError in httpx
        if _is_tls_failure(exc):
            return SSLError(
                message=f"SSL/TLS error: {exc}", url=url, original_error=exc
            )
        return NetworkError(
            message=f"Connection error: {exc}", url=url, original_error=exc
        )

    if isinstance(exc, module.NetworkError):
        return NetworkError(
            message=f"Network error: {exc}", url=url, original_error=exc
        )

    # Catch-all for any other HTTPError
    return NetworkError(message=f"HTTP error: {exc}", url=url, original_error=exc)


def _is_tls_failure(exc: Exception) -> bool:
    text = str(exc)
    return "SSL" in text or "TLS" in text or "certificate" in text.lower()


class HttpxAdapterBase:
    """
    HTTP client adapter backed by an httpx-compatible module.

    Subclasses bind a concrete module by setting ``_module`` (and may narrow the
    ``client`` annotation to that module's Client type).

    Provides advanced features like connection pooling, HTTP/2 support,
    and better performance than stdlib.
    """

    _module: ClassVar[HttpxLikeModule]

    client: Any

    def __init__(
        self,
        base_url: str | None = None,
        client: Any | None = None,
        get_token: Callable[[], str] | None = None,
    ):
        """
        Initialize the adapter.

        Args:
            base_url: Optional base URL for all requests. Relative URLs will be joined to this.
            client: Optional pre-configured Client instance from this adapter's module.
                   If not provided, a new client will be created.
            get_token: Optional callback to get the current access token. Will be called
                      before each request to support token refresh.
        """
        self.get_token = get_token
        if client is not None:
            self.client = client
            self._owns_client = False
        else:
            self.client = self._module.Client(base_url=base_url or "")
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
    ) -> Result[HttpResponse, HttpxRequestError]:
        """Make an HTTP request."""
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
        except self._module.HTTPError as e:
            return Err(translate_transport_error(self._module, e, url, timeout))

        error = status_error(response)
        if error is not None:
            return Err(error)

        return Ok(cast(HttpResponse, HttpxResponse(response)))
