from collections.abc import Callable
from typing import Unpack

from src.id.models import CoreWebhook, CreateWebhookResponse
from src.satvu_api_sdk.core import SDKClient


class IDService(SDKClient):
    """"""

    base_path = "/id/v2/"

    def __init__(self, get_token: Callable[[], str], contract_id: str, env: str | None):
        self.contract_id = contract_id
        super().__init__(env=env, get_token=get_token, contract_id=contract_id)

    def post_webhooks(self, **kwargs: Unpack[CoreWebhook]) -> CreateWebhookResponse:
        response = self.make_request(
            method="POST", url="/webhooks/", json=kwargs, contract_id=self.contract_id
        )
        response.raise_for_status()

        return CreateWebhookResponse(**response.json())
