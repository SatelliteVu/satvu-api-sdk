import logging
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

from pydantic import BaseModel

from satvu_api_sdk.http import HttpClient, create_http_client
from satvu_api_sdk.http.errors import HttpError
from satvu_api_sdk.http.protocol import HttpResponse
from satvu_api_sdk.result import Result

logger = logging.getLogger(__name__)


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
        max_retry_attempts: int = 5,
        max_retry_after_seconds: float = 300.0,
    ):
        self.timeout = timeout
        self.max_retry_attempts = max_retry_attempts
        self.max_retry_after_seconds = max_retry_after_seconds
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
        Make an HTTP request with automatic Retry-After handling.

        Automatically retries requests when the server provides a Retry-After header
        for a 202 Accepted response, respecting the server's requested delay.
        The delay is capped at max_retry_after_seconds (default 5 minutes) and
        will retry up to max_retry_attempts times (default 5).

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
        for attempt in range(1, self.max_retry_attempts + 1):
            result = self._execute_request(
                method, url, json, params, follow_redirects, timeout
            )

            if result.is_err():
                return result

            response = result.unwrap()

            if response.status_code != 202:
                return result

            # Handle 202 with Retry-After
            retry_after = self._parse_retry_after_from_headers(
                response.headers, self.max_retry_after_seconds
            )
            if retry_after is None or attempt >= self.max_retry_attempts:
                return result

            # Log retry attempt
            logger.info(
                f"Received 202 Accepted - retrying in {retry_after:.0f}s "
                f"(attempt {attempt}/{self.max_retry_attempts})"
            )

            time.sleep(retry_after)

        return result

    def _execute_request(
        self,
        method: str,
        url: str,
        json: list | dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        follow_redirects: bool = False,
        timeout: int | None = None,
    ) -> Result[HttpResponse, HttpError]:
        """
        Execute HTTP request.

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
    def _parse_retry_after_from_headers(
        headers: dict[str, str] | None, max_seconds: float
    ) -> float | None:
        """
        Parse Retry-After header from response headers.

        Args:
            headers: Response headers dict (can be None)
            max_seconds: Maximum delay to cap at

        Returns:
            Delay in seconds (capped at max_seconds), or None if no header present.
        """
        if not headers:
            return None

        # Case-insensitive header lookup
        retry_after = next(
            (val for key, val in headers.items() if key.lower() == "retry-after"), None
        )

        if not retry_after:
            return None

        # Parse as integer seconds
        delay = float(retry_after)
        return min(delay, max_seconds)

    @staticmethod
    def stream_to_file(
        response: HttpResponse,
        output_path: Path | str,
        chunk_size: int = 8192,
        progress_callback: Callable[[int, int | None], None] | None = None,
    ) -> Path:
        """
        Stream HTTP response to disk with optional progress tracking.

        Memory-efficient: streams response in chunks without loading entire file into memory.
        Ideal for large file downloads (satellite imagery, archives, etc.).

        Args:
            response: HTTP response to stream
            output_path: Where to save the file (Path or string)
            chunk_size: Bytes per chunk (default: 8KB). Increase for better throughput
                       on fast connections (e.g., 64KB), decrease for progress granularity.
            progress_callback: Optional callback called after each chunk is written.
                             Signature: callback(bytes_downloaded: int, total_bytes: int | None)
                             total_bytes is None if Content-Length header is not present.

        Returns:
            Path object pointing to the downloaded file

        Note:
            This method uses response.iter_bytes() which can only be called once per response.
            The response stream is consumed during this operation.
        """
        output_path = Path(output_path)

        # Get total file size from Content-Length header (if available)
        total_bytes: int | None = None
        content_length = response.headers.get("Content-Length") or response.headers.get(
            "content-length"
        )
        if content_length:
            try:
                total_bytes = int(content_length)
            except (ValueError, TypeError):
                # Content-Length header exists but isn't a valid integer
                total_bytes = None

        # Stream response to disk in chunks
        bytes_downloaded = 0
        with output_path.open("wb") as f:
            for chunk in response.iter_bytes(chunk_size=chunk_size):
                f.write(chunk)
                bytes_downloaded += len(chunk)

                # Call progress callback if provided
                if progress_callback:
                    progress_callback(bytes_downloaded, total_bytes)

        return output_path

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
