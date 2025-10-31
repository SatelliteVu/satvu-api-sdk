"""Urllib3 HTTP adapter."""

from json import dumps, loads
from typing import Any
from urllib.parse import urlencode, urljoin

try:
    import urllib3
except ImportError:
    raise ImportError(
        "urllib3 is required to use Urllib3Adapter. "
        'Install it with: pip install "satvu-api-sdk[http-urllib3]"'
    )

from satvu_api_sdk.http.protocol import HttpMethod, HttpResponse


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
        return self._body

    @property
    def text(self) -> str:
        return self.body.decode("utf-8")

    def json(self) -> Any:
        return loads(self.text)


class Urllib3Adapter:
    """
    HTTP client adapter using urllib3 library.

    Provides lower-level HTTP functionality with connection pooling
    and more control over request/response handling.
    """

    def __init__(
        self, base_url: str = "", pool_manager: urllib3.PoolManager | None = None
    ):
        """
        Initialize the urllib3 adapter.

        Args:
            base_url: Base URL for all requests. Relative URLs will be joined to this.
            pool_manager: Optional pre-configured urllib3.PoolManager instance.
                         If not provided, a new one will be created.
        """
        self.base_url = base_url.rstrip("/") if base_url else ""

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
    ) -> HttpResponse:
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

        # Prepare headers
        req_headers = headers.copy() if headers else {}

        # Prepare body
        body_data: bytes | str | None = None
        if json is not None:
            body_data = dumps(json)
            req_headers["Content-Type"] = "application/json"
        elif data is not None:
            body_data = urlencode(data)
            req_headers["Content-Type"] = "application/x-www-form-urlencoded"

        # Make request
        response = self.pool_manager.request(
            method=method,
            url=full_url,
            headers=req_headers,
            body=body_data,
            timeout=timeout,
            redirect=follow_redirects,
        )

        return Urllib3Response(response)
