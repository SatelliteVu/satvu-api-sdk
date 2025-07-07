from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..models.point import Point
    from ..models.standard_order_request_properties_with_addons import (
        StandardOrderRequestPropertiesWithAddons,
    )


@dataclass
class StandardOrderRequest:
    """Feature model for incoming order request.

    Attributes:
        type (Literal['Feature']):
        geometry (Point): Point Model
        properties (StandardOrderRequestPropertiesWithAddons):
    """

    type: Literal["Feature"]
    geometry: "Point"
    properties: "StandardOrderRequestPropertiesWithAddons"

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "type",
            "geometry",
            "properties",
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
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
