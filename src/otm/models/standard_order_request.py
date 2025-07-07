from typing import Literal

from pydantic import BaseModel

from ..models.point import Point
from ..models.standard_order_request_properties_with_addons import (
    StandardOrderRequestPropertiesWithAddons,
)


class StandardOrderRequest(BaseModel):
    """Feature model for incoming order request.

    Attributes:
        type (Literal['Feature']):
        geometry (Point): Point Model
        properties (StandardOrderRequestPropertiesWithAddons):
    """

    type: Literal["Feature"]
    geometry: "Point"
    properties: "StandardOrderRequestPropertiesWithAddons"
