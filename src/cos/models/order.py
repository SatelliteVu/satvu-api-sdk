import datetime
from typing import Union
from uuid import UUID

from pydantic import BaseModel, Field

from ..models.price import Price
from ..models.stac_metadata import StacMetadata


class Order(BaseModel):
    """
    Attributes:
        item_id (Union[list[str], str]): The item ID.
        order_id (UUID): The order ID.
        created_at (datetime.datetime): The datetime at which the order was created.
        price (Price): Pricing information.
        stac_metadata (Union[None, StacMetadata]): Metadata about the item.
    """

    item_id: Union[list[str], str] = Field(..., description="The item ID.")
    order_id: UUID = Field(..., description="The order ID.")
    created_at: datetime.datetime = Field(
        ..., description="The datetime at which the order was created."
    )
    price: "Price" = Field(..., description="Pricing information.")
    stac_metadata: Union[None, StacMetadata] = Field(
        None, description="Metadata about the item."
    )
