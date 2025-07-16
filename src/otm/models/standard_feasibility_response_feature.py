from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel, Field

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

    type: Literal["Feature"] = Field("Feature", description=None)
    geometry: "Point" = Field(..., description="Point Model")
    properties: "StandardFeasibilityResponseProperties" = Field(
        ..., description="Properties of the standard priority feasibility response."
    )
    id: UUID = Field(..., description="The ID of the feasibility request.")
    bbox: Union[None, list[float]] = Field(None, description=None)
