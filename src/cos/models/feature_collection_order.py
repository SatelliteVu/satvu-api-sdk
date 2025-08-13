import datetime
from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from ..models.feature_order import FeatureOrder
from ..models.price import Price


class FeatureCollectionOrder(BaseModel):
    """
    Attributes:
        id (UUID): The order ID.
        features (list[FeatureOrder]): An array of Item objects.
        owned_by (str): The owner of the order.
        created_at (datetime.datetime): The datetime at which the order was created.
        contract_id (UUID): The contract ID.
        price (Price): Pricing information.
        type_ (Union[Literal['FeatureCollection'], None]):  Default: 'FeatureCollection'.
        name (Union[None, str]): The name of the order.
        updated_at (Union[None, datetime.datetime]): The datetime at which the order was updated.
    """

    id: UUID = Field(..., description="The order ID.", alias="id")
    features: list[FeatureOrder] = Field(
        ..., description="An array of Item objects.", alias="features"
    )
    owned_by: str = Field(..., description="The owner of the order.", alias="owned_by")
    created_at: datetime.datetime = Field(
        ...,
        description="The datetime at which the order was created.",
        alias="created_at",
    )
    contract_id: UUID = Field(..., description="The contract ID.", alias="contract_id")
    price: "Price" = Field(..., description="Pricing information.", alias="price")
    type_: Union[Literal["FeatureCollection"], None] = Field(
        "FeatureCollection", description=None, alias="type"
    )
    name: Union[None, str] = Field(
        None, description="The name of the order.", alias="name"
    )
    updated_at: Union[None, datetime.datetime] = Field(
        None,
        description="The datetime at which the order was updated.",
        alias="updated_at",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
