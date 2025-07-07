from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, Union

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.reseller_stored_order_request import ResellerStoredOrderRequest
    from ..models.response_context import ResponseContext
    from ..models.stored_order_request import StoredOrderRequest


@dataclass
class StoredOrderRequestList:
    """
    Attributes:
        type (Literal['FeatureCollection']):
        features (list[Union['ResellerStoredOrderRequest', 'StoredOrderRequest']]): List of stored order requests.
        links (list['Link']): Links to previous and/or next page.
        context (ResponseContext):
    """

    type: Literal["FeatureCollection"]
    features: list[Union["ResellerStoredOrderRequest", "StoredOrderRequest"]]
    links: list["Link"]
    context: "ResponseContext"

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "type",
            "features",
            "links",
            "context",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "type": object,
            "features": object,
            "links": object,
            "context": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
