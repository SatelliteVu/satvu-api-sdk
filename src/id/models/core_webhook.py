from typing import Union

from pydantic import BaseModel

from ..models.reseller_webhook_event import ResellerWebhookEvent
from ..models.webhook_event import WebhookEvent


class CoreWebhook(BaseModel):
    """
    Attributes:
        event_types (list[Union[ResellerWebhookEvent, WebhookEvent]]): A list of events to subscribe to.
        name (str): The name of the webhook.
        url (str): The URL where you want to receive requests for events you are subscribed to. Must be HTTPS.
    """

    event_types: list[Union[ResellerWebhookEvent, WebhookEvent]]
    name: str
    url: str
