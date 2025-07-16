from typing import Union

from pydantic import BaseModel, Field

from ..models.reseller_webhook_event import ResellerWebhookEvent
from ..models.webhook_event import WebhookEvent


class EditWebhookPayload(BaseModel):
    """
    Attributes:
        active (Union[None, bool]): Whether the webhook should be active or not.
        event_types (Union[None, list[Union[ResellerWebhookEvent, WebhookEvent]]]): A list of events to subscribe to.
        name (Union[None, str]): The name of the webhook.
    """

    active: Union[None, bool] = Field(
        None, description="Whether the webhook should be active or not."
    )
    event_types: Union[None, list[Union[ResellerWebhookEvent, WebhookEvent]]] = Field(
        None, description="A list of events to subscribe to."
    )
    name: Union[None, str] = Field(None, description="The name of the webhook.")
