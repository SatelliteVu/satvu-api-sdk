"""HTTPX HTTP adapter."""

from typing import Any

try:
    import httpx
except ImportError:
    raise ImportError(
        "httpx is required to use HTTPXAdapter. "
        'Install it with: pip install "satvu-api-sdk[http-httpx]"'
    )

from satvu_api_sdk.http.protocol import HttpMethod, HttpResponse


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
    def text(self) -> str:
        return self._response.text

    def json(self) -> Any:
        return self._response.json()


class HttpxAdapter:
    """
    HTTP client adapter using httpx library.

    Provides advanced features like connection pooling, HTTP/2 support,
    and better performance than stdlib.
    """

    def __init__(self, base_url: str = "", client: httpx.Client | None = None):
        """
        Initialize the httpx adapter.

        Args:
            base_url: Base URL for all requests. Relative URLs will be joined to this.
            client: Optional pre-configured httpx.Client instance. If not provided,
                   a new client will be created.
        """
        if client is not None:
            self.client = client
            self._owns_client = False
        else:
            self.client = httpx.Client(base_url=base_url)
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
    ) -> HttpResponse:
        """Make an HTTP request using httpx."""
        # Filter out None values from params
        if params:
            params = {k: v for k, v in params.items() if v is not None}

        response = self.client.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json,
            data=data,
            timeout=timeout,
            follow_redirects=follow_redirects,
        )

        return HttpxResponse(response)
