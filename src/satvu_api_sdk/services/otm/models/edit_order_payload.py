from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.order_name import OrderName


class EditOrderPayload(BaseModel):
    """Payload for editing an order.

    Attributes:
        properties (OrderName):
    """

    properties: "OrderName" = Field(..., description=None, alias="properties")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
