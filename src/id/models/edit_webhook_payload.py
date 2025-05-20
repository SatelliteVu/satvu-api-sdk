from dataclasses import dataclass
from typing import Union

from ..models.webhook_event import WebhookEvent
from ..types import UNSET, Unset


@dataclass
class EditWebhookPayload:
    """
    Attributes:
        active (Union[Unset, bool]): Whether the webhook should be active or not.
        event_types (Union[Unset, list[WebhookEvent]]): A list of events to subscribe to.
        name (Union[Unset, str]): The name of the webhook.
    """

    active: Union[Unset, bool] = UNSET
    event_types: Union[Unset, list[WebhookEvent]] = UNSET
    name: Union[Unset, str] = UNSET

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {}
