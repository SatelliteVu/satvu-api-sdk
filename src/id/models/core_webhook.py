from dataclasses import dataclass

from ..models.webhook_event import WebhookEvent


@dataclass
class CoreWebhook:
    """
    Attributes:
        event_types (list[WebhookEvent]): A list of events to subscribe to.
        name (str): The name of the webhook.
        url (str): The URL where you want to receive requests for events you are subscribed to. Must be HTTPS.
    """

    event_types: list[WebhookEvent]
    name: str
    url: str

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "event_types",
            "name",
            "url",
        }
