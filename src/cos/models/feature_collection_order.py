import datetime
from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel, Field

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

    id: UUID = Field(..., description="Order ID.")
    features: list["FeatureOrder"] = Field(..., description="An array of Item objects.")
    owned_by: str = Field(..., description="The owner of the order.")
    created_at: datetime.datetime = Field(
        ..., description="The datetime at which the order was created."
    )
    contract_id: UUID = Field(..., description="Contract ID.")
    price: "Price" = Field(..., description=None)
    type: Union[Literal["FeatureCollection"], None] = Field(
        "FeatureCollection", description=None
    )
    name: Union[None, str] = Field(None, description="The name of the order.")
    updated_at: Union[None, datetime.datetime] = Field(
        None, description="The datetime at which the order was updated."
    )
