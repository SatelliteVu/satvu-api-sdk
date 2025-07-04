import datetime
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, Union
from uuid import UUID

from ..types import Unset

if TYPE_CHECKING:
    from ..models.feature_order import FeatureOrder
    from ..models.price import Price


@dataclass
class FeatureCollectionOrder:
    """
    Attributes:
        id (UUID): Order ID.
        features (list['FeatureOrder']): An array of Item objects.
        owned_by (str): The owner of the order.
        created_at (datetime.datetime): The datetime at which the order was created.
        contract_id (UUID): Contract ID.
        price (Price):
        type (Union[Literal['FeatureCollection'], Unset]):  Default: 'FeatureCollection'.
        name (Union[None, str]): The name of the order.
        updated_at (Union[None, datetime.datetime]): The datetime at which the order was updated.
    """

    id: UUID
    features: list["FeatureOrder"]
    owned_by: str
    created_at: datetime.datetime
    contract_id: UUID
    price: "Price"
    type: Union[Literal["FeatureCollection"], Unset] = "FeatureCollection"
    name: Union[None, str] = None
    updated_at: Union[None, datetime.datetime] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "id",
            "features",
            "owned_by",
            "created_at",
            "contract_id",
            "price",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "id": UUID,
            "features": object,
            "owned_by": str,
            "created_at": object,
            "contract_id": UUID,
            "price": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "type": object,
            "name": object,
            "updated_at": object,
        }
