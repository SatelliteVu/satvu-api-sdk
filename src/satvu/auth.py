import os
from base64 import b64decode
from configparser import ConfigParser, DuplicateSectionError
from datetime import datetime
from hashlib import sha1
from json import loads
from logging import getLogger
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Protocol
from urllib.parse import urljoin

from pydantic import BaseModel, ValidationError

try:
    from appdirs import user_cache_dir  # type: ignore[import-not-found]
except ImportError:
    user_cache_dir = None

import contextlib

from satvu.core import SDKClient
from satvu.http import HttpClient
from satvu.http.errors import ClientError, ServerError
from satvu.result import Err, Ok, Result, is_err

logger = getLogger(__name__)


class AuthError(RuntimeError):
    pass


class OAuthTokenResponse(BaseModel):
    """OAuth token response containing access and refresh tokens."""

    access_token: str
    refresh_token: str | None = None


class TokenCache(Protocol):
    def save(self, client_id: str, value: OAuthTokenResponse): ...
    def load(self, client_id: str) -> OAuthTokenResponse | None: ...


class MemoryCache:
    def __init__(self):
        self._items: dict[str, OAuthTokenResponse] = {}

    def save(self, client_id: str, value: OAuthTokenResponse):
        self._items[client_id] = value

    def load(self, client_id: str) -> OAuthTokenResponse | None:
        return self._items.get(client_id)


class AppDirCache:
    """
    File based token cache using an INI file in the user's cache dir or given dir.
    """

    cache_dir: Path
    cache_file: Path

    def __init__(self, cache_dir: str | None = None):
        if user_cache_dir is None:
            raise RuntimeError(
                'To use the AppDirCache, please install "satvu[standard]": pip install "satvu[standard]"'
            )
        self.cache_dir = Path(cache_dir if cache_dir else user_cache_dir("SatelliteVu"))
        self.cache_file = self.cache_dir / "tokencache"

        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def save(self, client_id: str, value: OAuthTokenResponse):
        parser = ConfigParser()
        parser.read(self.cache_file)

        with contextlib.suppress(DuplicateSectionError):
            parser.add_section(client_id)
        parser[client_id]["access_token"] = value.access_token
        parser[client_id]["refresh_token"] = value.refresh_token or ""

        with NamedTemporaryFile("w", dir=str(self.cache_dir), delete=False) as handle:
            parser.write(handle)
        os.replace(handle.name, self.cache_file)

    def load(self, client_id: str) -> OAuthTokenResponse | None:
        try:
            parser = ConfigParser()
            parser.read(self.cache_file)

            cached = parser[client_id]
            return OAuthTokenResponse(
                access_token=cached["access_token"],
                refresh_token=cached["refresh_token"],
            )
        except (FileNotFoundError, KeyError):
            return None


class AuthService(SDKClient):
    base_path = "/oauth"

    def __init__(
        self,
        env: str | None,
        token_cache: TokenCache | None = None,
        http_client: HttpClient | None = None,
        timeout: int = 30,
    ):
        super().__init__(
            subdomain="auth",
            env=env,
            get_token=None,
            http_client=http_client,
            timeout=timeout,
        )
        self.audience = self.build_url("api")
        self.cache = token_cache or MemoryCache()

    @staticmethod
    def is_expired_token(token: str) -> bool:
        """
        Check if a JWT token is expired based on its exp claim.

        Returns True if the token is expired or malformed (fail-safe).
        """
        try:
            parts = token.split(".")
            if len(parts) != 3:
                return True  # Invalid JWT format
            json_data = b64decode(parts[1] + "==")
            claims = loads(json_data)
            if not claims or "exp" not in claims:
                return True  # No exp claim, treat as expired
            exp = float(claims["exp"])
            return datetime.fromtimestamp(exp) <= datetime.now()
        except (ValueError, IndexError, KeyError, TypeError):
            return True  # Any parsing error = treat as expired

    def token(
        self, client_id: str, client_secret: str, scopes: list[str] | None = None
    ) -> Result[str, AuthError]:
        """
        Get an OAuth access token, using cache if available.

        Args:
            client_id: OAuth client ID
            client_secret: OAuth client secret
            scopes: Optional list of OAuth scopes

        Returns:
            Result containing either:
            - Ok(str) with the access token
            - Err(AuthError) if authentication fails
        """
        scopes = scopes or []
        cache_key = sha1(client_id.encode("utf-8"), usedforsecurity=False)
        cache_key.update("".join(scopes).encode("utf-8"))

        cached_token = self.cache.load(cache_key.hexdigest())

        if not cached_token or self.is_expired_token(cached_token.access_token):
            auth_result = self._auth(client_id, client_secret, scopes)
            if is_err(auth_result):
                return auth_result  # Propagate error

            token = auth_result.unwrap()
            self.cache.save(cache_key.hexdigest(), token)
        else:
            token = cached_token

        return Ok(token.access_token)

    def _auth(
        self,
        client_id: str,
        client_secret: str,
        scopes: list[str],
    ) -> Result[OAuthTokenResponse, AuthError]:
        """
        Perform OAuth client credentials authentication.

        Args:
            client_id: OAuth client ID
            client_secret: OAuth client secret
            scopes: List of OAuth scopes to request

        Returns:
            Result containing either:
            - Ok(OAuthTokenResponse) with access and refresh tokens
            - Err(AuthError) if authentication fails
        """
        logger.info("performing client_credential authentication")
        token_url = urljoin(self.base_path, "token")

        result = self.client.request(
            "POST",
            token_url,
            headers={"content-type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "client_credentials",
                "client_id": client_id,
                "client_secret": client_secret,
                "audience": self.audience,
                "scope": " ".join(scopes),
            },
            timeout=float(self.timeout),
        )

        # Handle Result type
        if is_err(result):
            error = result.error()
            # Distinguish between HTTP status errors and transport errors
            if isinstance(error, ClientError | ServerError):
                # HTTP error response (4xx/5xx) - server responded with error status
                body_text = (
                    error.response_body.decode("utf-8") if error.response_body else ""
                )
                return Err(
                    AuthError(
                        f"Auth request failed with status {error.status_code}: {body_text}"
                    )
                )
            # Transport error (network, timeout, SSL, etc.)
            return Err(AuthError(f"HTTP request failed: {error}"))

        response = result.unwrap()

        if response.status_code != 200:
            text = response.text.unwrap_or("")
            return Err(
                AuthError(
                    "Unexpected error code for client_credential flow: "
                    f"{response.status_code} - {text}"
                )
            )

        # Parse JSON response
        json_result = response.json()
        if is_err(json_result):
            error = json_result.error()
            return Err(
                AuthError(
                    f"Unexpected response body for client_credential flow: {error}"
                )
            )

        payload = json_result.unwrap()

        # Parse into Pydantic model for validation
        try:
            token_response = OAuthTokenResponse(**payload)
        except ValidationError as e:
            return Err(AuthError(f"Invalid token response structure: {e}"))

        return Ok(token_response)
