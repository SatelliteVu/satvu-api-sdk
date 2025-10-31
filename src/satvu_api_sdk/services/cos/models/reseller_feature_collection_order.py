from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Literal, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.feature_order import FeatureOrder
    from ..models.price import Price


class ResellerFeatureCollectionOrder(BaseModel):
    """
    Attributes:
        reseller_end_user_id (UUID): The ID of the end user for whom the order is placed for.
        id (UUID): The order ID.
        features (list[FeatureOrder]): An array of Item objects.
        owned_by (str): The owner of the order.
        created_at (datetime.datetime): The datetime at which the order was created.
        contract_id (UUID): The contract ID.
        price (Price): Pricing information.
        type_ (Union[Literal['FeatureCollection'], None]):  Default: 'FeatureCollection'.
        name (None | str): The name of the order.
        updated_at (datetime.datetime | None): The datetime at which the order was updated.
        licence_level (None | str): Licence level applied to the order. Licences are contract-specific.
    """

    reseller_end_user_id: UUID = Field(
        ...,
        description="The ID of the end user for whom the order is placed for.",
        alias="reseller_end_user_id",
    )
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
    name: None | str = Field(None, description="The name of the order.", alias="name")
    updated_at: datetime.datetime | None = Field(
        None,
        description="The datetime at which the order was updated.",
        alias="updated_at",
    )
    licence_level: None | str = Field(
        None,
        description="Licence level applied to the order. Licences are contract-specific.",
        alias="licence_level",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
