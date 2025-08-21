from __future__ import annotations

from typing import TYPE_CHECKING, Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.geo_json_point import GeoJSONPoint
    from ..models.standard_order_request_properties import (
        StandardOrderRequestProperties,
    )


class ResellerStandardOrderRequest(BaseModel):
    """
    Attributes:
        type_ (Literal['Feature']):
        geometry (GeoJSONPoint):
        properties (StandardOrderRequestProperties):
        reseller_end_user_id (UUID):
    """

    type_: Literal["Feature"] = Field("Feature", description=None, alias="type")
    geometry: "GeoJSONPoint" = Field(..., description=None, alias="geometry")
    properties: "StandardOrderRequestProperties" = Field(
        ..., description=None, alias="properties"
    )
    reseller_end_user_id: UUID = Field(
        ..., description=None, alias="reseller_end_user_id"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
