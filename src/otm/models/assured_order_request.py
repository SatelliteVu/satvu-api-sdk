from pydantic import BaseModel, Field

from ..models.assured_order_request_properties import AssuredOrderRequestProperties


class AssuredOrderRequest(BaseModel):
    """
    Attributes:
        properties (AssuredOrderRequestProperties):
    """

    properties: "AssuredOrderRequestProperties" = Field(..., description=None)
