from id.api import IdService
from satvu_api_sdk.auth import AuthService, TokenCache


class SatVuSDK:
    """ """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        contract_id: str | None,
        env: str | None = None,
        token_cache: TokenCache | None = None,
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.contract_id = contract_id
        self.token_cache = token_cache
        self.env = env

        # for lazy service initialisation
        self._auth = None
        self._id = None

    def get_token(self):
        return self.auth.token(self.client_id, self.client_secret)

    def auth(self):
        if not self._auth:
            self._auth = AuthService(env=self.env, token_cache=self.token_cache)
        return self._auth

    @property
    def id(self):
        if not self._id:
            self._id = IdService(
                env=self.env
            )
        return self._id
