from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.list_response_context import ListResponseContext
    from ..models.webhook_response import WebhookResponse


class ListWebhookResponse(BaseModel):
    """
    Attributes:
        webhooks (list[WebhookResponse]): List of webhooks.
        context (ListResponseContext):
        links (list[Link]): Links to previous and/or next page.
    """

    webhooks: list[WebhookResponse] = Field(
        ..., description="List of webhooks.", alias="webhooks"
    )
    context: "ListResponseContext" = Field(..., description=None, alias="context")
    links: list[Link] = Field(
        ..., description="Links to previous and/or next page.", alias="links"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
