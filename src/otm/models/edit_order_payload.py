from pydantic import BaseModel, Field

from ..models.order_name import OrderName


class EditOrderPayload(BaseModel):
    """Payload for editing an order.

    Attributes:
        properties (OrderName):
    """

    properties: "OrderName" = Field(..., description=None)
