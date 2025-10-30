"""Standard library HTTP adapter using urllib."""

import json as json_lib
import warnings
from http.client import HTTPResponse as StdlibHTTPResponse
from typing import Any
from urllib.error import HTTPError
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen

from satvu_api_sdk.http.protocol import HttpMethod, HttpResponse


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
    def text(self) -> str:
        return self.body.decode("utf-8")

    def json(self) -> Any:
        return json_lib.loads(self.text)


class StdlibAdapter:
    """
    HTTP client adapter using Python's standard library (urllib).

    Zero external dependencies. Suitable for minimal installations.
    """

    def __init__(self, base_url: str = ""):
        """
        Initialize the stdlib adapter.

        Args:
            base_url: Base URL for all requests. Relative URLs will be joined to this.
        """
        self.base_url = base_url.rstrip("/") if base_url else ""

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

        # Prepare headers
        req_headers = headers.copy() if headers else {}

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
            return StdlibResponse(response, full_url)
        except HTTPError as e:
            # HTTPError is also a valid response, just with error status
            return StdlibResponse(e, full_url)
