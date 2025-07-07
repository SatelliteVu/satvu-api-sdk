from uuid import UUID

from pydantic import BaseModel

from ..models.assured_order_request_properties import AssuredOrderRequestProperties


class ResellerAssuredOrderRequest(BaseModel):
    """
    Attributes:
        properties (AssuredOrderRequestProperties):
        reseller_end_user_id (UUID):
    """

    properties: "AssuredOrderRequestProperties"
    reseller_end_user_id: UUID
