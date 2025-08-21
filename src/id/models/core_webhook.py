from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.reseller_webhook_event import ResellerWebhookEvent
from ..models.webhook_event import WebhookEvent


class CoreWebhook(BaseModel):
    """
    Attributes:
        event_types (list[Union['ResellerWebhookEvent', 'WebhookEvent']]): A list of events to subscribe to.
        name (str): The name of the webhook.
        url (str): The URL where you want to receive requests for events you are subscribed to. Must be HTTPS.
    """

    event_types: list[Union["ResellerWebhookEvent", "WebhookEvent"]] = Field(
        ..., description="A list of events to subscribe to.", alias="event_types"
    )
    name: str = Field(..., description="The name of the webhook.", alias="name")
    url: str = Field(
        ...,
        description="The URL where you want to receive requests for events you are subscribed to. Must be HTTPS.",
        alias="url",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
