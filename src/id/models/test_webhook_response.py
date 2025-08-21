from __future__ import annotations

from typing import TYPE_CHECKING, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.notification_description import NotificationDescription
    from ..models.reseller_notification_description import (
        ResellerNotificationDescription,
    )
    from ..models.webhook_result import WebhookResult


class TestWebhookResponse(BaseModel):
    """
    Attributes:
        active (bool): Whether the webhook is active.
        event_types (list[Union['NotificationDescription', 'ResellerNotificationDescription']]): List of events that the
            webhook is subscribed to.
        name (str): The name of the webhook.
        url (str): The URL where events are received.
        id (UUID): A unique identifier for the webhook.
        webhook_result (WebhookResult):
    """

    active: bool = Field(
        ..., description="Whether the webhook is active.", alias="active"
    )
    event_types: list[
        Union["NotificationDescription", "ResellerNotificationDescription"]
    ] = Field(
        ...,
        description="List of events that the webhook is subscribed to.",
        alias="event_types",
    )
    name: str = Field(..., description="The name of the webhook.", alias="name")
    url: str = Field(..., description="The URL where events are received.", alias="url")
    id: UUID = Field(
        ..., description="A unique identifier for the webhook.", alias="id"
    )
    webhook_result: "WebhookResult" = Field(
        ..., description=None, alias="webhook_result"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
