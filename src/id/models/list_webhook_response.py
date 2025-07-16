from pydantic import BaseModel, Field

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

    webhooks: list["WebhookResponse"] = Field(..., description="List of webhooks.")
    context: "ListResponseContext" = Field(..., description=None)
    links: list["Link"] = Field(..., description="Links to previous and/or next page.")
