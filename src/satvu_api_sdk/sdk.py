from demo.main import IDService
from satvu_api_sdk.auth import AuthService


class SatVuSDK:
    """
    """

    def __init__(self, contract_id: str | None, env: str | None = None):
        self._auth = None
        self._id = None
        self.contract_id = contract_id
        self.env = env

    def get_token(self):
        return ""

    def auth(self):
        if not self._auth:
            self._auth = AuthService(env=self.env)
        return self._auth

    @property
    def id(self):
        if not self._id:
            self._id = IDService(self.get_token, contract_id=self.contract_id, env=self.env)
        return self._id
