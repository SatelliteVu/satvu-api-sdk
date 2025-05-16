import datetime
from typing import TYPE_CHECKING, TypedDict, Union
from uuid import UUID

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price import Price
    from ..models.stac_metadata import StacMetadata


class Order(TypedDict):
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
