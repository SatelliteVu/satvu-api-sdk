import datetime
from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel

from ..models.feature_order import FeatureOrder
from ..models.price import Price


class ResellerFeatureCollectionOrder(BaseModel):
    """
    Attributes:
        id (UUID): Order ID.
        features (list['FeatureOrder']): An array of Item objects.
        owned_by (str): The owner of the order.
        created_at (datetime.datetime): The datetime at which the order was created.
        contract_id (UUID): Contract ID.
        price (Price):
        reseller_end_user_id (UUID):
        type (Union[Literal['FeatureCollection'], None]):  Default: 'FeatureCollection'.
        name (Union[None, str]): The name of the order.
        updated_at (Union[None, datetime.datetime]): The datetime at which the order was updated.
    """

    id: UUID
    features: list["FeatureOrder"]
    owned_by: str
    created_at: datetime.datetime
    contract_id: UUID
    price: "Price"
    reseller_end_user_id: UUID
    type: Union[Literal["FeatureCollection"], None] = "FeatureCollection"
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
            "reseller_end_user_id",
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
            "reseller_end_user_id": UUID,
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
