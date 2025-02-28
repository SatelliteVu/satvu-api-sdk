from satvu_api_sdk.core import SDKClient


class AuthService(SDKClient):

    def __init__(self, env: str | None):
        super().__init__(subdomain="auth", env=env, get_token=None)