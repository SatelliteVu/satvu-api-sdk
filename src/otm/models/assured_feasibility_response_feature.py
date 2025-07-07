from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel

from ..models.assured_feasibility_response_properties import (
    AssuredFeasibilityResponseProperties,
)
from ..models.point import Point


class AssuredFeasibilityResponseFeature(BaseModel):
    """Object representing an assured feasibility response.

    Attributes:
        type (Literal['Feature']):
        geometry (Point): Point Model
        properties (AssuredFeasibilityResponseProperties): Properties of the assured priority feasibility response.
        id (UUID): The ID of the feasibility request.
        signature (str): Signature token
        bbox (Union[None, list[float]]):
    """

    type: Literal["Feature"]
    geometry: "Point"
    properties: "AssuredFeasibilityResponseProperties"
    id: UUID
    signature: str
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
            "signature",
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
            "signature": str,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "bbox": object,
        }
