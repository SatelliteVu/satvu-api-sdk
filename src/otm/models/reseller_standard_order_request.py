from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field

from ..models.point import Point
from ..models.standard_order_request_properties_with_addons import (
    StandardOrderRequestPropertiesWithAddons,
)


class ResellerStandardOrderRequest(BaseModel):
    """
    Attributes:
        type (Literal['Feature']):
        geometry (Point): Point Model
        properties (StandardOrderRequestPropertiesWithAddons):
        reseller_end_user_id (UUID):
    """

    type: Literal["Feature"] = Field("Feature", description=None)
    geometry: "Point" = Field(..., description="Point Model")
    properties: "StandardOrderRequestPropertiesWithAddons" = Field(
        ..., description=None
    )
    reseller_end_user_id: UUID = Field(..., description=None)
