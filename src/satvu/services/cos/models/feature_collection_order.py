# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Literal
from uuid import UUID

import pydantic

if TYPE_CHECKING:
    from ..models.feature_order import FeatureOrder
    from ..models.order_pricing import OrderPricing


class FeatureCollectionOrder(pydantic.BaseModel):
    """
    Attributes:
        id (UUID): The order ID.
        features (list[FeatureOrder]): An array of Item objects.
        owned_by (str): The owner of the order.
        created_at (datetime.datetime): The datetime at which the order was created.
        contract_id (UUID): The contract ID.
        price (OrderPricing): Detailed pricing breakdown for a satellite imagery order, including base price and license
            uplifts.
        type_ (Literal['FeatureCollection']):  Default: 'FeatureCollection'.
        name (None | str): The name of the order.
        updated_at (datetime.datetime | None): The datetime at which the order was updated.
        licence_level (None | str): Licence level applied to the order. Licences are contract-specific. Nullable for
            orders created before licensing was introduced.
    """

    id: UUID = pydantic.Field(..., description="""The order ID.""", alias="id")
    features: list[FeatureOrder] = pydantic.Field(
        ..., description="""An array of Item objects.""", alias="features"
    )
    owned_by: str = pydantic.Field(
        ..., description="""The owner of the order.""", alias="owned_by"
    )
    created_at: datetime.datetime = pydantic.Field(
        ...,
        description="""The datetime at which the order was created.""",
        alias="created_at",
    )
    contract_id: UUID = pydantic.Field(
        ..., description="""The contract ID.""", alias="contract_id"
    )
    price: OrderPricing = pydantic.Field(
        ...,
        description="""Detailed pricing breakdown for a satellite imagery order, including base price and license uplifts.""",
        alias="price",
    )
    type_: Literal["FeatureCollection"] = pydantic.Field(
        default="FeatureCollection", description=None, alias="type"
    )
    name: None | str = pydantic.Field(
        default=None, description="""The name of the order.""", alias="name"
    )
    updated_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description="""The datetime at which the order was updated.""",
        alias="updated_at",
    )
    licence_level: None | str = pydantic.Field(
        default=None,
        description="""Licence level applied to the order. Licences are contract-specific. Nullable for orders created before licensing was introduced.""",
        alias="licence_level",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
