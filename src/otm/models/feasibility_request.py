from typing import Literal, Union

from pydantic import BaseModel

from ..models.assured_feasibility_fields import AssuredFeasibilityFields
from ..models.point import Point
from ..models.standard_order_request_properties import StandardOrderRequestProperties


class FeasibilityRequest(BaseModel):
    """Feature model for incoming feasibility request.

    Attributes:
        type (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union[AssuredFeasibilityFields, StandardOrderRequestProperties]): A dictionary of additional
            metadata about the requested image.
    """

    type: Literal["Feature"] = "Feature"
    geometry: "Point"
    properties: Union[AssuredFeasibilityFields, StandardOrderRequestProperties]
