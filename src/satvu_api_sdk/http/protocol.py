"""HTTP client protocol definitions for SDK adapters."""

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Literal, Protocol

if TYPE_CHECKING:
    from satvu_api_sdk.http.errors import HttpError, JsonDecodeError, TextDecodeError
    from satvu_api_sdk.result import Result

HttpMethod = Literal["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"]


class HttpResponse(Protocol):
    """Protocol defining the interface for HTTP responses across different libraries."""

    @property
    def status_code(self) -> int:
        """HTTP status code of the response."""
        ...

    @property
    def headers(self) -> dict[str, str]:
        """Response headers as a dictionary."""
        ...

    @property
    def body(self) -> bytes:
        """
        Raw response body as bytes.

        Loads the entire response into memory. For large responses (e.g., file downloads),
        use iter_bytes() instead to stream the response in chunks.
        """
        ...

    def iter_bytes(self, chunk_size: int = 8192) -> Iterator[bytes]:
        """
        Stream response body in chunks without loading it all into memory.

        This method is ideal for downloading large files (e.g., satellite imagery)
        as it yields chunks incrementally instead of loading the entire response.

        Args:
            chunk_size: Number of bytes to read per chunk (default: 8KB)

        Yields:
            Chunks of bytes from the response body

        Important:
            - Can only be called once per response
            - Cannot use .body property after calling this (response is consumed)
            - If .body was already accessed, this will yield the cached body in chunks

        Example:
            >>> result = client.request("GET", "https://api.example.com/large-file.zip")
            >>> response = result.unwrap()
            >>> with open("output.zip", "wb") as f:
            ...     for chunk in response.iter_bytes(chunk_size=65536):
            ...         f.write(chunk)
        """
        ...

    @property
    def text(self) -> "Result[str, TextDecodeError]":
        """
        Response body decoded as text.

        Returns:
            Ok(str) with decoded text, or Err(TextDecodeError) if decoding fails
        """
        ...

    def json(self) -> "Result[Any, JsonDecodeError | TextDecodeError]":
        """
        Parse response body as JSON.

        Returns:
            Ok(parsed_json) on success, or Err(JsonDecodeError | TextDecodeError) if parsing fails
        """
        ...


class HttpClient(Protocol):
    """Protocol defining the interface for HTTP clients across different libraries."""

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
    ) -> "Result[HttpResponse, HttpError]":
        """
        Make an HTTP request.

        Args:
            method: HTTP method (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS)
            url: URL to request (can be relative to base_url if supported)
            headers: Optional HTTP headers
            params: Optional query parameters
            json: Optional JSON body (will be serialized)
            data: Optional form data (for form-encoded requests)
            timeout: Request timeout in seconds
            follow_redirects: Whether to follow redirects

        Returns:
            Result containing either:
            - Ok(HttpResponse) on success (including 2xx and 3xx responses)
            - Err(HttpError) on failure, which can be:
                - NetworkError: Connection failures, DNS errors
                - ConnectionTimeoutError: Timeout establishing connection
                - ReadTimeoutError: Timeout reading response
                - SSLError: Certificate/TLS errors
                - ProxyError: Proxy connection/auth failures
                - ClientError: HTTP 4xx responses
                - ServerError: HTTP 5xx responses
                - RequestValidationError: Invalid parameters

        Example:
            >>> result = client.request("GET", "https://api.example.com/data")
            >>> match result:
            ...     case Ok(response):
            ...         print(f"Success: {response.status_code}")
            ...     case Err(error):
            ...         print(f"Failed: {error}")
        """
        ...
