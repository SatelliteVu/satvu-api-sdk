from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel

from ..models.point import Point
from ..models.standard_feasibility_response_properties import (
    StandardFeasibilityResponseProperties,
)


class StandardFeasibilityResponseFeature(BaseModel):
    """Object representing a standard feasibility response.

    Attributes:
        type (Literal['Feature']):
        geometry (Point): Point Model
        properties (StandardFeasibilityResponseProperties): Properties of the standard priority feasibility response.
        id (UUID): The ID of the feasibility request.
        bbox (Union[None, list[float]]):
    """

    type: Literal["Feature"]
    geometry: "Point"
    properties: "StandardFeasibilityResponseProperties"
    id: UUID
    bbox: Union[None, list[float]] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "type",
            "geometry",
            "properties",
            "id",
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
            "id": UUID,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "bbox": object,
        }
