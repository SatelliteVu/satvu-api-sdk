from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal
from uuid import UUID

if TYPE_CHECKING:
    from ..models.point import Point
    from ..models.standard_order_request_properties_with_addons import (
        StandardOrderRequestPropertiesWithAddons,
    )


@dataclass
class ResellerStandardOrderRequest:
    """
    Attributes:
        type (Literal['Feature']):
        geometry (Point): Point Model
        properties (StandardOrderRequestPropertiesWithAddons):
        reseller_end_user_id (UUID):
    """

    type: Literal["Feature"]
    geometry: "Point"
    properties: "StandardOrderRequestPropertiesWithAddons"
    reseller_end_user_id: UUID

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "type",
            "geometry",
            "properties",
            "reseller_end_user_id",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "type": object,
            "geometry": object,
            "properties": object,
            "reseller_end_user_id": UUID,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
