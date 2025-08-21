from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.geo_json_point import GeoJSONPoint
    from ..models.standard_order_request_properties import (
        StandardOrderRequestProperties,
    )


class StandardOrderRequest(BaseModel):
    """Feature model for incoming order request.

    Attributes:
        type_ (Literal['Feature']):
        geometry (GeoJSONPoint):
        properties (StandardOrderRequestProperties):
    """

    type_: Literal["Feature"] = Field("Feature", description=None, alias="type")
    geometry: "GeoJSONPoint" = Field(..., description=None, alias="geometry")
    properties: "StandardOrderRequestProperties" = Field(
        ..., description=None, alias="properties"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
