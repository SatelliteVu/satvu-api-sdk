from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Literal, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.assured_feasibility_fields_with_addons import (
        AssuredFeasibilityFieldsWithAddons,
    )
    from ..models.point import Point
    from ..models.price_information import PriceInformation
    from ..models.standard_order_fields_with_addons import StandardOrderFieldsWithAddons


class OrderPrice(BaseModel):
    """
    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union['AssuredFeasibilityFieldsWithAddons', 'StandardOrderFieldsWithAddons']): A map of additional
            metadata about the requested image.
        created_at (datetime.datetime): The current UTC time.
        price (PriceInformation): Pricing information.
    """

    type_: Literal["Feature"] = Field("Feature", description=None, alias="type")
    geometry: "Point" = Field(..., description="Point Model", alias="geometry")
    properties: Union[
        "AssuredFeasibilityFieldsWithAddons", "StandardOrderFieldsWithAddons"
    ] = Field(
        ...,
        description="A map of additional metadata about the requested image.",
        alias="properties",
    )
    created_at: datetime.datetime = Field(
        ..., description="The current UTC time.", alias="created_at"
    )
    price: "PriceInformation" = Field(
        ..., description="Pricing information.", alias="price"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
