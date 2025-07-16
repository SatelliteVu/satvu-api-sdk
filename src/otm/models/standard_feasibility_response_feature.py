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

    type: Literal["Feature"] = "Feature"
    geometry: "Point"
    properties: "StandardFeasibilityResponseProperties"
    id: UUID
    bbox: Union[None, list[float]] = None
