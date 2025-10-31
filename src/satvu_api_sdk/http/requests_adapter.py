"""Requests HTTP adapter."""

from typing import Any

try:
    import requests
except ImportError:
    raise ImportError(
        "requests is required to use RequestsAdapter. "
        'Install it with: pip install "satvu-api-sdk[http-requests]"'
    )

from satvu_api_sdk.http.protocol import HttpMethod, HttpResponse


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
    def text(self) -> str:
        return self._response.text

    def json(self) -> Any:
        return self._response.json()


class RequestsAdapter:
    """
    HTTP client adapter using requests library.

    The most popular HTTP library in Python, known for its simple
    and elegant API. Widely used and well-documented.
    """

    def __init__(self, base_url: str = "", session: requests.Session | None = None):
        """
        Initialize the requests adapter.

        Args:
            base_url: Base URL for all requests. Relative URLs will be joined to this.
            session: Optional pre-configured requests.Session instance. If not provided,
                    a new session will be created.
        """
        self.base_url = base_url.rstrip("/") if base_url else ""

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
    ) -> HttpResponse:
        """Make an HTTP request using requests."""
        # Build full URL
        if self.base_url and not url.startswith(("http://", "https://")):
            full_url = f"{self.base_url}/{url.lstrip('/')}"
        else:
            full_url = url

        # Filter out None values from params
        if params:
            params = {k: v for k, v in params.items() if v is not None}

        # Make request
        response = self.session.request(
            method=method,
            url=full_url,
            headers=headers,
            params=params,
            json=json,
            data=data,
            timeout=timeout,
            allow_redirects=follow_redirects,
        )

        return RequestsResponse(response)
