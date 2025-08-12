from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from ..models.point import Point
from ..models.standard_order_request_properties import StandardOrderRequestProperties


class StandardOrderRequest(BaseModel):
    """Feature model for incoming order request.

    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (StandardOrderRequestProperties):
    """

    type_: Literal["Feature"] = Field("Feature", description=None, alias="type")
    geometry: "Point" = Field(..., description="Point Model", alias="geometry")
    properties: "StandardOrderRequestProperties" = Field(
        ..., description=None, alias="properties"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
