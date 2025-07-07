from pydantic import BaseModel

from ..models.link import Link
from ..models.list_response_context import ListResponseContext
from ..models.webhook_response import WebhookResponse


class ListWebhookResponse(BaseModel):
    """
    Attributes:
        webhooks (list['WebhookResponse']): List of webhooks.
        context (ListResponseContext):
        links (list['Link']): Links to previous and/or next page.
    """

    webhooks: list["WebhookResponse"]
    context: "ListResponseContext"
    links: list["Link"]
