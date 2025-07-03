from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.list_response_context import ListResponseContext
    from ..models.webhook_response import WebhookResponse


@dataclass
class ListWebhookResponse:
    """
    Attributes:
        webhooks (list['WebhookResponse']): List of webhooks.
        context (ListResponseContext):
        links (list['Link']): Links to previous and/or next page.
    """

    webhooks: list["WebhookResponse"]
    context: "ListResponseContext"
    links: list["Link"]

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "webhooks",
            "context",
            "links",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "webhooks": object,
            "context": object,
            "links": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
