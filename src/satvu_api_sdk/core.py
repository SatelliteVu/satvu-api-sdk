from collections.abc import Callable

import httpx


class SDKClient:
    """ """

    base_path: str

    def __init__(
        self,
        env: str | None,
        get_token: Callable[[], str] | None = None,
        subdomain: str = "api",
    ):
        base_url = f"{self.build_url(subdomain, env=env).rstrip('/')}/{self.base_path.lstrip('/')}"
        if get_token:
            auth_token = get_token()
            self.client = httpx.Client(
                base_url=base_url, headers={"Authorization": f"Bearer {auth_token}"}
            )
        else:
            self.client = httpx.Client(base_url=base_url)

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
        json: list | dict | None = None,
        params: dict | None = None,
        follow_redirects: bool = False,
        timeout: int = 5,
    ):
        return self.client.request(
            method=method,
            url=url,
            json=json,
            params=params,
            follow_redirects=follow_redirects,
            timeout=timeout,
        )
