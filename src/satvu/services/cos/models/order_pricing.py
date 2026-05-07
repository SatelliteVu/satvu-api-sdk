# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class OrderPricing(BaseModel):
    """Detailed pricing breakdown for a satellite imagery order, including base price and license uplifts.

    Attributes:
        currency (str): The currency of the order.
        base (int): The base price of the order in minor units of the currency e.g. pence, cents.
        licence_level (int): The price of the order due to the licence level uplift in minor units of the currency e.g.
            pence, cents.
        total (int): The total price of the order in minor units of the currency e.g. pence, cents. This is the sum of
            the base and licence level prices.
        total_uplift (int): The sum of all uplifts, including licencing, applied to the order in minor units of the
            currency e.g. pence, cents.
    """

    currency: str = Field(
        ..., description="""The currency of the order.""", alias="currency"
    )
    base: int = Field(
        ...,
        description="""The base price of the order in minor units of the currency e.g. pence, cents.""",
        alias="base",
    )
    licence_level: int = Field(
        ...,
        description="""The price of the order due to the licence level uplift in minor units of the currency e.g. pence, cents.""",
        alias="licence_level",
    )
    total: int = Field(
        ...,
        description="""The total price of the order in minor units of the currency e.g. pence, cents. This is the sum of the base and licence level prices.""",
        alias="total",
    )
    total_uplift: int = Field(
        ...,
        description="""The sum of all uplifts, including licencing, applied to the order in minor units of the currency e.g. pence, cents.""",
        alias="total_uplift",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
