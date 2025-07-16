from uuid import UUID

from pydantic import BaseModel, Field

from ..models.assured_order_request_properties import AssuredOrderRequestProperties


class ResellerAssuredOrderRequest(BaseModel):
    """
    Attributes:
        properties (AssuredOrderRequestProperties):
        reseller_end_user_id (UUID):
    """

    properties: "AssuredOrderRequestProperties" = Field(..., description=None)
    reseller_end_user_id: UUID = Field(..., description=None)
