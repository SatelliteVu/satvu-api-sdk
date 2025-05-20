import datetime
from dataclasses import dataclass
from typing import TYPE_CHECKING, Union
from uuid import UUID

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price import Price
    from ..models.stac_metadata import StacMetadata


@dataclass
class Order:
    """
    Attributes:
        item_id (Union[list[str], str]): Item ID.
        order_id (UUID): Order ID.
        created_at (datetime.datetime): The datetime at which the order was created.
        price (Price):
        stac_metadata (Union['StacMetadata', None, Unset]): Metadata about the item.
    """

    item_id: Union[list[str], str]
    order_id: UUID
    created_at: datetime.datetime
    price: "Price"
    stac_metadata: Union["StacMetadata", None, Unset] = UNSET

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "item_id",
            "order_id",
            "created_at",
            "price",
        }
