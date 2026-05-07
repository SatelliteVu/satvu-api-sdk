# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.order_item_price import OrderItemPrice
    from ..models.stac_metadata import StacMetadata


class Order(BaseModel):
    """
    Attributes:
        item_id (str): The item ID.
        order_id (UUID): The order ID.
        created_at (datetime.datetime): The datetime at which the order was created.
        price (OrderItemPrice): Price information for an individual imagery item within an order.
        stac_metadata (Union['StacMetadata', None]): Metadata about the item.
    """

    item_id: str = Field(..., description="""The item ID.""", alias="item_id")
    order_id: UUID = Field(..., description="""The order ID.""", alias="order_id")
    created_at: datetime.datetime = Field(
        ...,
        description="""The datetime at which the order was created.""",
        alias="created_at",
    )
    price: OrderItemPrice = Field(
        ...,
        description="""Price information for an individual imagery item within an order.""",
        alias="price",
    )
    stac_metadata: Union[StacMetadata, None] = Field(
        default=None, description="""Metadata about the item.""", alias="stac_metadata"
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
