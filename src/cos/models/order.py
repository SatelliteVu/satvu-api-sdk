import datetime
from dataclasses import dataclass
from typing import TYPE_CHECKING, Union
from uuid import UUID

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
        name (Union[None, str]): Optional name of an order
        stac_metadata (Union['StacMetadata', None]): Metadata about the item.
    """

    item_id: Union[list[str], str]
    order_id: UUID
    created_at: datetime.datetime
    price: "Price"
    name: Union[None, str] = None
    stac_metadata: Union["StacMetadata", None] = None

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

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "item_id": object,
            "order_id": UUID,
            "created_at": object,
            "price": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "name": object,
            "stac_metadata": object,
        }
