from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from ..models.assured_order_request_properties import AssuredOrderRequestProperties


class ResellerAssuredOrderRequest(BaseModel):
    """
    Attributes:
        properties (AssuredOrderRequestProperties):
        reseller_end_user_id (UUID):
    """

    properties: "AssuredOrderRequestProperties" = Field(
        ..., description=None, alias="properties"
    )
    reseller_end_user_id: UUID = Field(
        ..., description=None, alias="reseller_end_user_id"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
