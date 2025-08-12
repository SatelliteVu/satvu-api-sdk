from typing import Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from ..models.point import Point
from ..models.standard_order_request_properties import StandardOrderRequestProperties


class ResellerStandardOrderRequest(BaseModel):
    """
    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (StandardOrderRequestProperties):
        reseller_end_user_id (UUID):
    """

    type_: Literal["Feature"] = Field("Feature", description=None, alias="type")
    geometry: "Point" = Field(..., description="Point Model", alias="geometry")
    properties: "StandardOrderRequestProperties" = Field(
        ..., description=None, alias="properties"
    )
    reseller_end_user_id: UUID = Field(
        ..., description=None, alias="reseller_end_user_id"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
