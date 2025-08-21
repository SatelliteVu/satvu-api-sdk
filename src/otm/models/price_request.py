from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.assured_feasibility_fields_with_addons import (
        AssuredFeasibilityFieldsWithAddons,
    )
    from ..models.geo_json_point import GeoJSONPoint
    from ..models.standard_price_request_properties import (
        StandardPriceRequestProperties,
    )


class PriceRequest(BaseModel):
    """Feature model for incoming price request

    Attributes:
        type_ (Literal['Feature']):
        geometry (GeoJSONPoint):
        properties (Union['AssuredFeasibilityFieldsWithAddons', 'StandardPriceRequestProperties']): A dictionary of
            additional metadata about the requested image.
    """

    type_: Literal["Feature"] = Field("Feature", description=None, alias="type")
    geometry: "GeoJSONPoint" = Field(..., description=None, alias="geometry")
    properties: Union[
        "AssuredFeasibilityFieldsWithAddons", "StandardPriceRequestProperties"
    ] = Field(
        ...,
        description="A dictionary of additional metadata about the requested image.",
        alias="properties",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
