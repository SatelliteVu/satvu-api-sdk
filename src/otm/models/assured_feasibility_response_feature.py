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

    type: Literal["Feature"] = "Feature"
    geometry: "Point"
    properties: "AssuredFeasibilityResponseProperties"
    id: UUID
    signature: str
    bbox: Union[None, list[float]] = None
