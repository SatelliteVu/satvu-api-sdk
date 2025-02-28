from typing import TYPE_CHECKING, TypedDict
from uuid import UUID

if TYPE_CHECKING:
    from ..models.notification_description import NotificationDescription


class PostWebhookResponse(TypedDict):
    """
    Attributes:
        active (bool): Whether the webhook is active.
        event_types (list['NotificationDescription']): List of events that the webhook is subscribed to.
        name (str): The name of the webhook.
        url (str): The URL where events are received.
        id (UUID): A unique identifier for the webhook.
        signing_key (str): The webhook signing key for payload decryption.
    """

    active: bool
    event_types: list["NotificationDescription"]
    name: str
    url: str
    id: UUID
    signing_key: str
