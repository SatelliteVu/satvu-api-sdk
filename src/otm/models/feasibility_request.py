from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, Union

if TYPE_CHECKING:
    from ..models.assured_feasibility_fields import AssuredFeasibilityFields
    from ..models.point import Point
    from ..models.standard_order_request_properties import (
        StandardOrderRequestProperties,
    )


@dataclass
class FeasibilityRequest:
    """Feature model for incoming feasibility request.

    Attributes:
        type (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union['AssuredFeasibilityFields', 'StandardOrderRequestProperties']): A dictionary of additional
            metadata about the requested image.
    """

    type: Literal["Feature"]
    geometry: "Point"
    properties: Union["AssuredFeasibilityFields", "StandardOrderRequestProperties"]

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
