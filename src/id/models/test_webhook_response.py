from typing import Union
from uuid import UUID

from pydantic import BaseModel, Field

from ..models.notification_description import NotificationDescription
from ..models.reseller_notification_description import ResellerNotificationDescription
from ..models.webhook_result import WebhookResult


class TestWebhookResponse(BaseModel):
    """
    Attributes:
        active (bool): Whether the webhook is active.
        event_types (list[Union[NotificationDescription, ResellerNotificationDescription]]): List of events that the
            webhook is subscribed to.
        name (str): The name of the webhook.
        url (str): The URL where events are received.
        id (UUID): A unique identifier for the webhook.
        webhook_result (WebhookResult):
    """

    active: bool = Field(..., description="Whether the webhook is active.")
    event_types: list[
        Union[NotificationDescription, ResellerNotificationDescription]
    ] = Field(..., description="List of events that the webhook is subscribed to.")
    name: str = Field(..., description="The name of the webhook.")
    url: str = Field(..., description="The URL where events are received.")
    id: UUID = Field(..., description="A unique identifier for the webhook.")
    webhook_result: "WebhookResult" = Field(..., description=None)
