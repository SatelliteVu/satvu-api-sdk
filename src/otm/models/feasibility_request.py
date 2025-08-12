from typing import Literal, Union

from pydantic import BaseModel, Field

from ..models.assured_feasibility_fields import AssuredFeasibilityFields
from ..models.point import Point
from ..models.standard_request_properties import StandardRequestProperties


class FeasibilityRequest(BaseModel):
    """Feature model for incoming feasibility request.

    Attributes:
        type (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union[AssuredFeasibilityFields, StandardRequestProperties]): A dictionary of additional metadata
            about the requested image.
    """

    type: Literal["Feature"] = Field("Feature", description=None)
    geometry: "Point" = Field(..., description="Point Model")
    properties: Union[AssuredFeasibilityFields, StandardRequestProperties] = Field(
        ...,
        description="A dictionary of additional metadata about the requested image.",
    )
