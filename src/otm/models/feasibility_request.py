from typing import Literal, Union

from pydantic import BaseModel, Field

from ..models.assured_feasibility_fields import AssuredFeasibilityFields
from ..models.point import Point
from ..models.standard_order_request_properties import StandardOrderRequestProperties


class FeasibilityRequest(BaseModel):
    """Feature model for incoming feasibility request.

    Attributes:
        type (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union[AssuredFeasibilityFields, StandardOrderRequestProperties]): A dictionary of additional
            metadata about the requested image.
    """

    type: Literal["Feature"] = Field("Feature", description=None)
    geometry: "Point" = Field(..., description="Point Model")
    properties: Union[AssuredFeasibilityFields, StandardOrderRequestProperties] = Field(
        ...,
        description="A dictionary of additional metadata about the requested image.",
    )
