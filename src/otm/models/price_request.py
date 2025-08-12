from typing import Literal, Union

from pydantic import BaseModel, Field

from ..models.assured_feasibility_fields_with_addons import (
    AssuredFeasibilityFieldsWithAddons,
)
from ..models.point import Point
from ..models.standard_price_request_properties import StandardPriceRequestProperties


class PriceRequest(BaseModel):
    """Feature model for incoming price request

    Attributes:
        type (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union[AssuredFeasibilityFieldsWithAddons, StandardPriceRequestProperties]): A dictionary of
            additional metadata about the requested image.
    """

    type: Literal["Feature"] = Field("Feature", description=None)
    geometry: "Point" = Field(..., description="Point Model")
    properties: Union[
        AssuredFeasibilityFieldsWithAddons, StandardPriceRequestProperties
    ] = Field(
        ...,
        description="A dictionary of additional metadata about the requested image.",
    )
