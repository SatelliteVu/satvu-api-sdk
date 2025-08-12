import datetime
from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel, Field

from ..models.feature_order import FeatureOrder
from ..models.price import Price


class ResellerFeatureCollectionOrder(BaseModel):
    """
    Attributes:
        reseller_end_user_id (UUID): The ID of the end user for whom the order is placed for.
        id (UUID): The order ID.
        features (list['FeatureOrder']): An array of Item objects.
        owned_by (str): The owner of the order.
        created_at (datetime.datetime): The datetime at which the order was created.
        contract_id (UUID): The contract ID.
        price (Price): Pricing information.
        type (Union[Literal['FeatureCollection'], None]):  Default: 'FeatureCollection'.
        name (Union[None, str]): The name of the order.
        updated_at (Union[None, datetime.datetime]): The datetime at which the order was updated.
    """

    reseller_end_user_id: UUID = Field(
        ..., description="The ID of the end user for whom the order is placed for."
    )
    id: UUID = Field(..., description="The order ID.")
    features: list["FeatureOrder"] = Field(..., description="An array of Item objects.")
    owned_by: str = Field(..., description="The owner of the order.")
    created_at: datetime.datetime = Field(
        ..., description="The datetime at which the order was created."
    )
    contract_id: UUID = Field(..., description="The contract ID.")
    price: "Price" = Field(..., description="Pricing information.")
    type: Union[Literal["FeatureCollection"], None] = Field(
        "FeatureCollection", description=None
    )
    name: Union[None, str] = Field(None, description="The name of the order.")
    updated_at: Union[None, datetime.datetime] = Field(
        None, description="The datetime at which the order was updated."
    )
