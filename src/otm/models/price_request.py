from typing import Literal, Union

from pydantic import BaseModel

from ..models.assured_feasibility_fields_with_addons import (
    AssuredFeasibilityFieldsWithAddons,
)
from ..models.point import Point
from ..models.standard_order_request_properties_with_addons import (
    StandardOrderRequestPropertiesWithAddons,
)


class PriceRequest(BaseModel):
    """Feature model for incoming price request

    Attributes:
        type (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union[AssuredFeasibilityFieldsWithAddons, StandardOrderRequestPropertiesWithAddons]): A dictionary
            of additional metadata about the requested image.
    """

    type: Literal["Feature"]
    geometry: "Point"
    properties: Union[
        AssuredFeasibilityFieldsWithAddons, StandardOrderRequestPropertiesWithAddons
    ]
