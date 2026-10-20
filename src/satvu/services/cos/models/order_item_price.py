# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class OrderItemPrice(pydantic.BaseModel):
    """Price information for an individual imagery item within an order.

    Attributes:
        item_price (int): The price of the image in minor units of the currency e.g. pence, cents.
        currency (str): The currency of the order.
    """

    item_price: int = pydantic.Field(
        ...,
        description="""The price of the image in minor units of the currency e.g. pence, cents.""",
        alias="item_price",
    )
    currency: str = pydantic.Field(
        ..., description="""The currency of the order.""", alias="currency"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
