# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class OrderSubmissionPayload(BaseModel):
    """Request payload for submitting an order.

    Attributes:
        item_id (list[str] | str): The acquisition item ID(s) from the STAC catalog. Note: Only acquisition items are
            accepted. SBT, Primary, and Visual products cannot be ordered directly.
        licence_level (str): The licence level for the order. Licence levels are specific to the contract.
        name (None | str): The optional name of the order
    """

    item_id: list[str] | str = Field(
        ...,
        description="""The acquisition item ID(s) from the STAC catalog. Note: Only acquisition items are accepted. SBT, Primary, and Visual products cannot be ordered directly.""",
        alias="item_id",
    )
    licence_level: str = Field(
        ...,
        description="""The licence level for the order. Licence levels are specific to the contract.""",
        alias="licence_level",
    )
    name: None | str = Field(
        default=None, description="""The optional name of the order""", alias="name"
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
