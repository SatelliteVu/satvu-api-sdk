import datetime
from typing import Literal, Union

from pydantic import BaseModel

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

    type: Literal["Feature"] = "Feature"
    geometry: "Point"
    properties: Union[AssuredFeasibilityFieldsWithAddons, StandardOrderFieldsWithAddons]
    created_at: datetime.datetime
    price: "Price1"
