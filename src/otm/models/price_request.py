from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.assured_feasibility_fields_with_addons import (
    AssuredFeasibilityFieldsWithAddons,
)
from ..models.point import Point
from ..models.standard_price_request_properties import StandardPriceRequestProperties


class PriceRequest(BaseModel):
    """Feature model for incoming price request

    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union[AssuredFeasibilityFieldsWithAddons, StandardPriceRequestProperties]): A dictionary of
            additional metadata about the requested image.
    """

    type_: Literal["Feature"] = Field("Feature", description=None, alias="type")
    geometry: "Point" = Field(..., description="Point Model", alias="geometry")
    properties: Union[
        AssuredFeasibilityFieldsWithAddons, StandardPriceRequestProperties
    ] = Field(
        ...,
        description="A dictionary of additional metadata about the requested image.",
        alias="properties",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
