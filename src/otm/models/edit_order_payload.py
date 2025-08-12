from pydantic import BaseModel, ConfigDict, Field

from ..models.order_name import OrderName


class EditOrderPayload(BaseModel):
    """Payload for editing an order.

    Attributes:
        properties (OrderName):
    """

    properties: "OrderName" = Field(..., description=None, alias="properties")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
