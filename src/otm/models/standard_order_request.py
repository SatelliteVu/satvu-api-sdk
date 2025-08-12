from typing import Literal

from pydantic import BaseModel, Field

from ..models.point import Point
from ..models.standard_order_request_properties import StandardOrderRequestProperties


class StandardOrderRequest(BaseModel):
    """Feature model for incoming order request.

    Attributes:
        type (Literal['Feature']):
        geometry (Point): Point Model
        properties (StandardOrderRequestProperties):
    """

    type: Literal["Feature"] = Field("Feature", description=None)
    geometry: "Point" = Field(..., description="Point Model")
    properties: "StandardOrderRequestProperties" = Field(..., description=None)
