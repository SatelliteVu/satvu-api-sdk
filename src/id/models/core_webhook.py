from typing import TypedDict

from ..models.webhook_event import WebhookEvent


class CoreWebhook(TypedDict):
    """
    Attributes:
        event_types (list[WebhookEvent]): A list of events to subscribe to.
        name (str): The name of the webhook.
        url (str): The URL where you want to receive requests for events you are subscribed to. Must be HTTPS.
    """

    event_types: list[WebhookEvent]
    name: str
    url: str
