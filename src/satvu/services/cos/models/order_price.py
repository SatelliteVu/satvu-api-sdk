# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING

import pydantic

if TYPE_CHECKING:
    from ..models.price_information import PriceInformation


class OrderPrice(pydantic.BaseModel):
    """
    Attributes:
        item_id (list[str] | str): The acquisition item ID(s) from the STAC catalog. Note: Only acquisition items are
            accepted. SBT, Primary, and Visual products cannot be ordered directly.
        created_at (datetime.datetime): The datetime at which the order pricing was requested.
        price (PriceInformation):
        name (None | str): The optional name of the order
        licence_level (None | str): The licence level for the order. Licence levels are specific to the contract. Must
            be provided unless the `baseprice` query parameter is set to true.
    """

    item_id: list[str] | str = pydantic.Field(
        ...,
        description="""The acquisition item ID(s) from the STAC catalog. Note: Only acquisition items are accepted. SBT, Primary, and Visual products cannot be ordered directly.""",
        alias="item_id",
    )
    created_at: datetime.datetime = pydantic.Field(
        ...,
        description="""The datetime at which the order pricing was requested.""",
        alias="created_at",
    )
    price: PriceInformation = pydantic.Field(..., description=None, alias="price")
    name: None | str = pydantic.Field(
        default=None, description="""The optional name of the order""", alias="name"
    )
    licence_level: None | str = pydantic.Field(
        default=None,
        description="""The licence level for the order. Licence levels are specific to the contract. Must be provided unless the `baseprice` query parameter is set to true.""",
        alias="licence_level",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
