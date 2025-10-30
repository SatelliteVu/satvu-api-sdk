"""HTTP client protocol definitions for SDK adapters."""

from typing import Any, Literal, Protocol

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
        """Raw response body as bytes."""
        ...

    @property
    def text(self) -> str:
        """Response body decoded as text."""
        ...

    def json(self) -> Any:
        """Parse response body as JSON."""
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
    ) -> HttpResponse:
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
            HttpResponse object
        """
        ...
