from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.price import Price
    from ..models.stac_metadata_1 import StacMetadata1


class Order1(BaseModel):
    """
    Attributes:
        item_id (list[str] | str): The item ID.
        order_id (UUID): The order ID.
        created_at (datetime.datetime): The datetime at which the order was created.
        price (Price): Pricing information.
        stac_metadata (Union['StacMetadata1', None]): Metadata about the item.
    """

    item_id: list[str] | str = Field(..., description="The item ID.", alias="item_id")
    order_id: UUID = Field(..., description="The order ID.", alias="order_id")
    created_at: datetime.datetime = Field(
        ...,
        description="The datetime at which the order was created.",
        alias="created_at",
    )
    price: "Price" = Field(..., description="Pricing information.", alias="price")
    stac_metadata: Union["StacMetadata1", None] = Field(
        None, description="Metadata about the item.", alias="stac_metadata"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
