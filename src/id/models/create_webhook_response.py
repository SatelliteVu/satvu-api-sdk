from dataclasses import dataclass
from typing import TYPE_CHECKING, Union
from uuid import UUID

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_description import NotificationDescription
    from ..models.reseller_notification_description import (
        ResellerNotificationDescription,
    )


@dataclass
class CreateWebhookResponse:
    """
    Attributes:
        active (bool): Whether the webhook is active.
        event_types (list[Union['NotificationDescription', 'ResellerNotificationDescription']]): List of events that the
            webhook is subscribed to.
        name (str): The name of the webhook.
        url (str): The URL where events are received.
        id (UUID): A unique identifier for the webhook.
        signing_key (str): The webhook signing key for payload decryption.
        unreachable_warning (Union[Unset, str]): An optional warning if the URL is not reachable.
    """

    active: bool
    event_types: list[
        Union["NotificationDescription", "ResellerNotificationDescription"]
    ]
    name: str
    url: str
    id: UUID
    signing_key: str
    unreachable_warning: Union[Unset, str] = UNSET

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
            "signing_key",
        }
