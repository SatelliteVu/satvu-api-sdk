# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

import pydantic

if TYPE_CHECKING:
    from ..models.get_order_response import GetOrderResponse


class OrderModificationPrice(pydantic.BaseModel):
    """An order before and after an edit, each with its price.

    Attributes:
        original_order (GetOrderResponse): An order.
        updated_order (GetOrderResponse): An order.
    """

    original_order: GetOrderResponse = pydantic.Field(
        ..., description="""An order.""", alias="original_order"
    )
    updated_order: GetOrderResponse = pydantic.Field(
        ..., description="""An order.""", alias="updated_order"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
