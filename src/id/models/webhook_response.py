from dataclasses import dataclass
from typing import TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:
    from ..models.notification_description import NotificationDescription


@dataclass
class WebhookResponse:
    """
    Attributes:
        active (bool): Whether the webhook is active.
        event_types (list['NotificationDescription']): List of events that the webhook is subscribed to.
        name (str): The name of the webhook.
        url (str): The URL where events are received.
        id (UUID): A unique identifier for the webhook.
    """

    active: bool
    event_types: list["NotificationDescription"]
    name: str
    url: str
    id: UUID

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "active",
            "event_types",
            "name",
            "url",
            "id",
        }
