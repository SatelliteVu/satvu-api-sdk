from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Literal, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.assured_feasibility_fields_with_addons import (
        AssuredFeasibilityFieldsWithAddons,
    )
    from ..models.geo_json_point import GeoJSONPoint
    from ..models.price_1 import Price1
    from ..models.standard_order_fields_with_addons import StandardOrderFieldsWithAddons


class OrderPrice(BaseModel):
    """
    Attributes:
        type_ (Literal['Feature']):
        geometry (GeoJSONPoint):
        properties (Union['AssuredFeasibilityFieldsWithAddons', 'StandardOrderFieldsWithAddons']): A dictionary of
            additional metadata about the requested image.
        created_at (datetime.datetime): The current UTC time.
        price (Price1):
    """

    type_: Literal["Feature"] = Field("Feature", description=None, alias="type")
    geometry: "GeoJSONPoint" = Field(..., description=None, alias="geometry")
    properties: Union[
        "AssuredFeasibilityFieldsWithAddons", "StandardOrderFieldsWithAddons"
    ] = Field(
        ...,
        description="A dictionary of additional metadata about the requested image.",
        alias="properties",
    )
    created_at: datetime.datetime = Field(
        ..., description="The current UTC time.", alias="created_at"
    )
    price: "Price1" = Field(..., description=None, alias="price")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
