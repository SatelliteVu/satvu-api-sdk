from collections.abc import Callable
from typing import Any

from pydantic import BaseModel

from satvu_api_sdk.http import HttpClient, create_http_client
from satvu_api_sdk.result import is_err


class SDKClient:
    """ """

    base_path: str

    def __init__(
        self,
        env: str | None,
        get_token: Callable[[], str] | None = None,
        subdomain: str = "api",
        http_client: HttpClient | None = None,
    ):
        base_url = f"{self.build_url(subdomain, env=env).rstrip('/')}/{self.base_path.lstrip('/')}"

        if http_client is not None:
            self.client = http_client
        elif get_token:
            auth_token = get_token()
            self.client = create_http_client(
                "auto",
                base_url=base_url,
                headers={"Authorization": f"Bearer {auth_token}"},
            )
        else:
            self.client = create_http_client("auto", base_url=base_url)

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
        timeout: int = 5,
    ):
        if params:
            # Convert any pydantic model objects in params to json-serializable dicts
            for key, val in params.items():
                if isinstance(val, BaseModel):
                    params[key] = val.model_dump()

            # Drop any params that are None
            params = {k: v for k, v in params.items() if v}

        result = self.client.request(
            method=method,  # type: ignore
            url=url,
            json=json,
            params=params,
            follow_redirects=follow_redirects,
            timeout=float(timeout),
        )

        # Handle Result type - raise exception on error
        if is_err(result):
            raise result.error()

        # Return response for backward compatibility
        return result.unwrap()
