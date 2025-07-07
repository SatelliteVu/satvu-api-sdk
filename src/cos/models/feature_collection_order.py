import datetime
from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel

from ..models.feature_order import FeatureOrder
from ..models.price import Price


class FeatureCollectionOrder(BaseModel):
    """
    Attributes:
        id (UUID): Order ID.
        features (list['FeatureOrder']): An array of Item objects.
        owned_by (str): The owner of the order.
        created_at (datetime.datetime): The datetime at which the order was created.
        contract_id (UUID): Contract ID.
        price (Price):
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
    type: Union[Literal["FeatureCollection"], None] = "FeatureCollection"
    name: Union[None, str] = None
    updated_at: Union[None, datetime.datetime] = None
