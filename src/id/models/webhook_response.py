from typing import Union
from uuid import UUID

from pydantic import BaseModel

from ..models.notification_description import NotificationDescription
from ..models.reseller_notification_description import ResellerNotificationDescription


class WebhookResponse(BaseModel):
    """
    Attributes:
        active (bool): Whether the webhook is active.
        event_types (list[Union[NotificationDescription, ResellerNotificationDescription]]): List of events that the
            webhook is subscribed to.
        name (str): The name of the webhook.
        url (str): The URL where events are received.
        id (UUID): A unique identifier for the webhook.
    """

    active: bool
    event_types: list[Union[NotificationDescription, ResellerNotificationDescription]]
    name: str
    url: str
    id: UUID
