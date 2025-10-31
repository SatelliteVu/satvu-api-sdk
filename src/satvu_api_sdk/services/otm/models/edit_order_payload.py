from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.edit_order_properties import EditOrderProperties


class EditOrderPayload(BaseModel):
    """Payload for editing an order.

    Attributes:
        properties (EditOrderProperties): Properties that can be edited in an order.

            All fields are optional - only provided fields will be updated.
    """

    properties: "EditOrderProperties" = Field(
        ...,
        description="Properties that can be edited in an order.  All fields are optional - only provided fields will be updated.",
        alias="properties",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
