# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class PriceRequest(BaseModel):
    """Request payload for submitting an order.

    Attributes:
        item_id (list[str] | str): The acquisition item ID(s) from the STAC catalog. Note: Only acquisition items are
            accepted. SBT, Primary, and Visual products cannot be ordered directly.
        name (None | str): The optional name of the order
        licence_level (None | str): The licence level for the order. Licence levels are specific to the contract. Must
            be provided unless the `baseprice` query parameter is set to true.
    """

    item_id: list[str] | str = Field(
        ...,
        description="""The acquisition item ID(s) from the STAC catalog. Note: Only acquisition items are accepted. SBT, Primary, and Visual products cannot be ordered directly.""",
        alias="item_id",
    )
    name: None | str = Field(
        default=None, description="""The optional name of the order""", alias="name"
    )
    licence_level: None | str = Field(
        default=None,
        description="""The licence level for the order. Licence levels are specific to the contract. Must be provided unless the `baseprice` query parameter is set to true.""",
        alias="licence_level",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
