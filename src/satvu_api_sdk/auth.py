from base64 import b64decode
from configparser import ConfigParser, DuplicateSectionError
from datetime import datetime
from hashlib import sha1
from json import loads
from logging import getLogger
import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Protocol, TypedDict
from urllib.parse import urljoin

try:
    from appdirs import user_cache_dir
except ImportError:
    user_cache_dir = None

from satvu_api_sdk.core import SDKClient


logger = getLogger(__name__)


class AuthError(RuntimeError):
    pass


class OAuthTokenResponse(TypedDict):
    access_token: str
    refresh_token: str


class TokenCache(Protocol):
    def save(self, cache_key: str, value: OAuthTokenResponse): ...
    def load(self, cache_key: str) -> OAuthTokenResponse | None: ...


class MemoryCache:
    _items: dict[str, OAuthTokenResponse] = {}

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
            pkg = __package__.split(".")[0]
            raise RuntimeError(
                f'To use the AppDirCache, please install "{pkg}[standard]": pip install "{pkg}[standard]"'
            )
        self.cache_dir = Path(cache_dir if cache_dir else user_cache_dir("SatelliteVu"))
        self.cache_file = self.cache_dir / "tokencache"

        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def save(self, client_id: str, value: OAuthTokenResponse):
        parser = ConfigParser()
        parser.read(self.cache_file)

        try:
            parser.add_section(client_id)
        except DuplicateSectionError:
            pass
        parser[client_id]["access_token"] = value["access_token"]
        parser[client_id]["refresh_token"] = value["refresh_token"]

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

    def __init__(self, env: str | None, token_cache: TokenCache | None = None):
        super().__init__(subdomain="auth", env=env, get_token=None)
        self.audience = self.build_url("api", env=env)
        self.cache = token_cache or MemoryCache()

    @staticmethod
    def is_expired_token(token: str) -> bool:
        json = b64decode(token.split(".")[1] + "==")
        claims = loads(json)
        if not claims or "exp" not in claims:
            return False
        exp = float(claims["exp"])
        exp_dt = datetime.fromtimestamp(exp)
        return exp_dt <= datetime.now()

    def token(
        self, client_id: str, client_secret: str, scopes: list[str] | None = None
    ) -> str:
        scopes = scopes or []
        cache_key = sha1(client_id.encode("utf-8"))
        cache_key.update("".join(scopes).encode("utf-8"))

        token = self.cache.load(cache_key.hexdigest())

        if not token or self.is_expired_token(token):
            token = self._auth(client_id, client_secret, scopes)
            self.cache.save(cache_key.hexdigest(), token)

        return token["access_token"]

    def _auth(
        self,
        client_id: str,
        client_secret: str,
        scopes: list[str],
    ) -> OAuthTokenResponse:
        logger.info("performing client_credential authentication")
        token_url = urljoin(self.base_path, "token")
        response = self.client.post(
            token_url,
            headers={"content-type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "client_credentials",
                "client_id": client_id,
                "client_secret": client_secret,
                "audience": self.audience,
                "scope": " ".join(scopes),
            },
        )

        if response.status_code != 200:
            raise AuthError(
                "Unexpected error code for client_credential flow: "
                f"{response.status_code} - {response.text}"
            )
        try:
            payload = response.json()
            return payload
        except Exception:
            raise AuthError(
                "Unexpected response body for client_credential flow: " + response.text
            )
