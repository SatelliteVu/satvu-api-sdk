# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.price_information import PriceInformation


class ResellerOrderPrice(BaseModel):
    """Response payload for order price for a reseller.

    Attributes:
        reseller_end_user_id (UUID): The ID of the end user for whom the order is placed for.
        item_id (list[str] | str): The acquisition item ID(s) from the STAC catalog. Note: Only acquisition items are
            accepted. SBT, Primary, and Visual products cannot be ordered directly.
        created_at (datetime.datetime): The datetime at which the order pricing was requested.
        price (PriceInformation):
        name (None | str): The optional name of the order
        licence_level (None | str): The licence level for the order. Licence levels are specific to the contract. Must
            be provided unless the `baseprice` query parameter is set to true.
    """

    reseller_end_user_id: UUID = Field(
        ...,
        description="""The ID of the end user for whom the order is placed for.""",
        alias="reseller_end_user_id",
    )
    item_id: list[str] | str = Field(
        ...,
        description="""The acquisition item ID(s) from the STAC catalog. Note: Only acquisition items are accepted. SBT, Primary, and Visual products cannot be ordered directly.""",
        alias="item_id",
    )
    created_at: datetime.datetime = Field(
        ...,
        description="""The datetime at which the order pricing was requested.""",
        alias="created_at",
    )
    price: PriceInformation = Field(..., description=None, alias="price")
    name: None | str = Field(
        default=None, description="""The optional name of the order""", alias="name"
    )
    licence_level: None | str = Field(
        default=None,
        description="""The licence level for the order. Licence levels are specific to the contract. Must be provided unless the `baseprice` query parameter is set to true.""",
        alias="licence_level",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
