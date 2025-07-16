import datetime
from typing import Literal, Union

from pydantic import BaseModel, Field

from ..models.assured_feasibility_fields_with_addons import (
    AssuredFeasibilityFieldsWithAddons,
)
from ..models.point import Point
from ..models.price_1 import Price1
from ..models.standard_order_fields_with_addons import StandardOrderFieldsWithAddons


class OrderPrice(BaseModel):
    """
    Attributes:
        type (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union[AssuredFeasibilityFieldsWithAddons, StandardOrderFieldsWithAddons]): A dictionary of
            additional metadata about the requested image.
        created_at (datetime.datetime): The current UTC time.
        price (Price1):
    """

    type: Literal["Feature"] = Field("Feature", description=None)
    geometry: "Point" = Field(..., description="Point Model")
    properties: Union[
        AssuredFeasibilityFieldsWithAddons, StandardOrderFieldsWithAddons
    ] = Field(
        ...,
        description="A dictionary of additional metadata about the requested image.",
    )
    created_at: datetime.datetime = Field(..., description="The current UTC time.")
    price: "Price1" = Field(..., description=None)
