from dataclasses import dataclass
from typing import TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:
    from ..models.assured_order_request_properties import AssuredOrderRequestProperties


@dataclass
class ResellerAssuredOrderRequest:
    """
    Attributes:
        properties (AssuredOrderRequestProperties):
        reseller_end_user_id (UUID):
    """

    properties: "AssuredOrderRequestProperties"
    reseller_end_user_id: UUID

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "properties",
            "reseller_end_user_id",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "properties": object,
            "reseller_end_user_id": UUID,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
