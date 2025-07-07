from typing import Union

from pydantic import BaseModel

from ..models.reseller_webhook_event import ResellerWebhookEvent
from ..models.webhook_event import WebhookEvent


class EditWebhookPayload(BaseModel):
    """
    Attributes:
        active (Union[None, bool]): Whether the webhook should be active or not.
        event_types (Union[None, list[Union[ResellerWebhookEvent, WebhookEvent]]]): A list of events to subscribe to.
        name (Union[None, str]): The name of the webhook.
    """

    active: Union[None, bool] = None
    event_types: Union[None, list[Union[ResellerWebhookEvent, WebhookEvent]]] = None
    name: Union[None, str] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {}

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {}

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "active": bool,
            "event_types": object,
            "name": str,
        }
