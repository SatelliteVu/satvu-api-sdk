from pydantic import BaseModel

from ..models.order_name import OrderName


class EditOrderPayload(BaseModel):
    """Payload for editing an order.

    Attributes:
        properties (OrderName):
    """

    properties: "OrderName"
