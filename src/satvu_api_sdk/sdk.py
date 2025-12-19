from satvu_api_sdk.auth import AuthService, TokenCache
from satvu_api_sdk.http import HttpClient
from satvu_api_sdk.services.catalog.api import CatalogService
from satvu_api_sdk.services.cos.api import CosService
from satvu_api_sdk.services.id.api import IdService
from satvu_api_sdk.services.otm.api import OtmService
from satvu_api_sdk.services.policy.api import PolicyService
from satvu_api_sdk.services.reseller.api import ResellerService
from satvu_api_sdk.services.wallet.api import WalletService


class SatVuSDK:
    """Unified client for accessing SatVu's API services."""

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        env: str | None = None,
        token_cache: TokenCache | None = None,
        http_client: HttpClient | None = None,
        timeout: int = 30,
        max_retry_attempts: int = 5,
        max_retry_after_seconds: float = 300.0,
    ):
        """
        Initialize the SatVuSDK.

        :param client_id: the client ID for authentication
        :param client_secret: the client secret for authentication
        :param env: the environment to use
        :param token_cache: the token cache to use
        :param http_client: the HTTP client to use
        :param timeout: request timeout in seconds, defaults to 30 seconds
        :param max_retry_attempts: maximum number of retry attempts, default 5
        :param max_retry_after_seconds: maximum seconds to wait for Retry-After, default 300 seconds
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_cache = token_cache
        self.env = env
        self.http_client = http_client
        self.timeout = timeout
        self.max_retry_attempts = max_retry_attempts
        self.max_retry_after_seconds = max_retry_after_seconds

        # for lazy service initialisation
        self._auth = None
        self._catalog = None
        self._cos = None
        self._id = None
        self._otm = None
        self._policy = None
        self._reseller = None
        self._wallet = None

    def get_token(self) -> str:
        """Get authentication token, unwrapping the Result or raising on error."""
        return self.auth.token(self.client_id, self.client_secret).unwrap()

    @property
    def auth(self) -> AuthService:
        if not self._auth:
            self._auth = AuthService(
                env=self.env,
                token_cache=self.token_cache,
                http_client=self.http_client,
                timeout=self.timeout,
            )
        return self._auth

    @property
    def catalog(self) -> CatalogService:
        if not self._catalog:
            self._catalog = CatalogService(
                env=self.env,
                get_token=self.get_token,
                http_client=self.http_client,
                timeout=self.timeout,
                max_retry_attempts=self.max_retry_attempts,
                max_retry_after_seconds=self.max_retry_after_seconds,
            )
        return self._catalog

    @property
    def cos(self) -> CosService:
        if not self._cos:
            self._cos = CosService(
                env=self.env,
                get_token=self.get_token,
                http_client=self.http_client,
                timeout=self.timeout,
                max_retry_attempts=self.max_retry_attempts,
                max_retry_after_seconds=self.max_retry_after_seconds,
            )
        return self._cos

    @property
    def id(self) -> IdService:
        if not self._id:
            self._id = IdService(
                env=self.env,
                get_token=self.get_token,
                http_client=self.http_client,
                timeout=self.timeout,
                max_retry_attempts=self.max_retry_attempts,
                max_retry_after_seconds=self.max_retry_after_seconds,
            )
        return self._id

    @property
    def otm(self) -> OtmService:
        if not self._otm:
            self._otm = OtmService(
                env=self.env,
                get_token=self.get_token,
                http_client=self.http_client,
                timeout=self.timeout,
                max_retry_attempts=self.max_retry_attempts,
                max_retry_after_seconds=self.max_retry_after_seconds,
            )
        return self._otm

    @property
    def policy(self) -> PolicyService:
        if not self._policy:
            self._policy = PolicyService(
                env=self.env,
                get_token=self.get_token,
                http_client=self.http_client,
                timeout=self.timeout,
                max_retry_attempts=self.max_retry_attempts,
                max_retry_after_seconds=self.max_retry_after_seconds,
            )
        return self._policy

    @property
    def reseller(self) -> ResellerService:
        if not self._reseller:
            self._reseller = ResellerService(
                env=self.env,
                get_token=self.get_token,
                http_client=self.http_client,
                timeout=self.timeout,
                max_retry_attempts=self.max_retry_attempts,
                max_retry_after_seconds=self.max_retry_after_seconds,
            )
        return self._reseller

    @property
    def wallet(self) -> WalletService:
        if not self._wallet:
            self._wallet = WalletService(
                env=self.env,
                get_token=self.get_token,
                http_client=self.http_client,
                timeout=self.timeout,
                max_retry_attempts=self.max_retry_attempts,
                max_retry_after_seconds=self.max_retry_after_seconds,
            )
        return self._wallet
