from typing import Union
from uuid import UUID

from pydantic import BaseModel

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

    active: bool
    event_types: list[Union[NotificationDescription, ResellerNotificationDescription]]
    name: str
    url: str
    id: UUID
    webhook_result: "WebhookResult"

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
            "webhook_result",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "active": bool,
            "event_types": object,
            "name": str,
            "url": str,
            "id": UUID,
            "webhook_result": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
