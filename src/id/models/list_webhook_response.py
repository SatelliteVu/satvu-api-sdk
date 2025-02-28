from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.list_response_context import ListResponseContext
    from ..models.webhook_response import WebhookResponse


class ListWebhookResponse(TypedDict):
    """
    Attributes:
        webhooks (list['WebhookResponse']): List of webhooks.
        context (ListResponseContext):
        links (list['Link']): Links to previous and/or next page.
    """

    webhooks: list["WebhookResponse"]
    context: "ListResponseContext"
    links: list["Link"]
