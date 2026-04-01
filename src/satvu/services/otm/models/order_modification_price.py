# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.get_order_response import GetOrderResponse


class OrderModificationPrice(BaseModel):
    """Response model for order modification price estimates.

    Shows the complete before/after state of an order including all
    order properties (geometry, datetime, tasking parameters, status,
    id, contract_id, links, etc.) along with the pricing information
    for both states.

    This allows users to see:
    - What the order looks like currently (original_order)
    - What the order will look like after modification (updated_order)
    - The exact price impact of the change

        Attributes:
            original_order (GetOrderResponse): Payload for get order response.
            updated_order (GetOrderResponse): Payload for get order response.
    """

    original_order: GetOrderResponse = Field(
        ..., description="""Payload for get order response.""", alias="original_order"
    )
    updated_order: GetOrderResponse = Field(
        ..., description="""Payload for get order response.""", alias="updated_order"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
