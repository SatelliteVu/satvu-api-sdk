from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel, Field

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

    type: Literal["Feature"] = Field("Feature", description=None)
    geometry: "Point" = Field(..., description="Point Model")
    properties: "AssuredFeasibilityResponseProperties" = Field(
        ..., description="Properties of the assured priority feasibility response."
    )
    id: UUID = Field(..., description="The ID of the feasibility request.")
    signature: str = Field(..., description="Signature token")
    bbox: Union[None, list[float]] = Field(None, description=None)
