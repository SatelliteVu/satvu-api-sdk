from collections.abc import Callable
from typing import Any
from urllib.parse import parse_qs, urlparse

from pydantic import BaseModel

from satvu_api_sdk.http import HttpClient, create_http_client
from satvu_api_sdk.http.errors import HttpError
from satvu_api_sdk.http.protocol import HttpResponse
from satvu_api_sdk.result import Result


class SDKClient:
    """ """

    base_path: str

    def __init__(
        self,
        env: str | None,
        get_token: Callable[[], str] | None = None,
        subdomain: str = "api",
        http_client: HttpClient | None = None,
        timeout: int = 30,
    ):
        self.timeout = timeout
        base_url = f"{self.build_url(subdomain, env=env).rstrip('/')}/{self.base_path.lstrip('/')}"

        if http_client is not None:
            self.client = http_client
        else:
            self.client = create_http_client(
                "auto",
                base_url=base_url,
                get_token=get_token,
            )

    @staticmethod
    def build_url(subdomain: str, env: str | None):
        if not env:
            env = ""
        else:
            env = f"{env}."
        return f"https://{subdomain}.{env}satellitevu.com/"

    def make_request(
        self,
        method: str,
        url: str,
        json: list | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        follow_redirects: bool = False,
        timeout: int | None = None,
    ) -> Result[HttpResponse, HttpError]:
        """
        Make an HTTP request and return a Result.

        Args:
            method: HTTP method (GET, POST, PUT, PATCH, DELETE, etc.)
            url: URL to request
            json: Optional JSON body
            params: Optional query parameters
            follow_redirects: Whether to follow redirects
            timeout: Request timeout in seconds (uses instance timeout if None)

        Returns:
            Result containing either:
            - Ok(HttpResponse) on success
            - Err(HttpError) on failure
        """
        if params:
            # Convert any pydantic model objects in params to json-serializable dicts
            for key, val in params.items():
                if isinstance(val, BaseModel):
                    params[key] = val.model_dump()

            # Drop any params that are None
            params = {k: v for k, v in params.items() if v}

        # Use instance timeout if not specified
        timeout_val = timeout if timeout is not None else self.timeout

        return self.client.request(
            method=method,  # type: ignore
            url=url,
            json=json,
            params=params,
            follow_redirects=follow_redirects,
            timeout=float(timeout_val),
        )

    @staticmethod
    def extract_next_token(response: BaseModel) -> str | None:
        """
        Extract pagination token from STAC links array.

        Handles both GET (token in URL) and POST (token in body) patterns
        used across all SatVu APIs for pagination.

        Args:
            response: API response with links array

        Returns:
            Next pagination token or None if no more pages
        """
        if not hasattr(response, "links"):
            return None

        # Find link with rel="next"
        next_link = next(
            (link for link in response.links if link.rel == "next"),
            None,
        )

        if not next_link:
            return None

        # Method 1: GET request - token in URL query parameter
        if next_link.method == "GET":
            parsed = urlparse(next_link.href)
            params = parse_qs(parsed.query)
            return params.get("token", [None])[0]

        # Method 2: POST request - token in body
        if next_link.method == "POST" and next_link.body:
            if isinstance(next_link.body, dict):
                return next_link.body.get("token")
            if hasattr(next_link.body, "token"):
                return next_link.body.token

        return None
