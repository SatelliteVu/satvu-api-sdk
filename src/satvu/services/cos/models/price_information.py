# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class PriceInformation(BaseModel):
    """
    Attributes:
        currency (str): The currency of the order.
        base (int): The base price of the order in minor units of the currency e.g. pence, cents.
        final (bool): Whether the price is final. When the `baseprice` query parameter is true, this will be false as
            the price may change at order submission time after the required licence level has been accounted for.
        licence_level (int | None): The price of the order due to the licence level uplift in minor units of the
            currency e.g. pence, cents.
        total (int | None): The total price of the order in minor units of the currency e.g. pence, cents. This is the
            sum of the base and licence level prices.
        total_uplift (int | None): The sum of all uplifts, including licencing, applied to the order in minor units of
            the currency e.g. pence, cents.
    """

    currency: str = Field(
        ..., description="""The currency of the order.""", alias="currency"
    )
    base: int = Field(
        ...,
        description="""The base price of the order in minor units of the currency e.g. pence, cents.""",
        alias="base",
    )
    final: bool = Field(
        ...,
        description="""Whether the price is final. When the `baseprice` query parameter is true, this will be false as the price may change at order submission time after the required licence level has been accounted for.""",
        alias="final",
    )
    licence_level: int | None = Field(
        default=None,
        description="""The price of the order due to the licence level uplift in minor units of the currency e.g. pence, cents.""",
        alias="licence_level",
    )
    total: int | None = Field(
        default=None,
        description="""The total price of the order in minor units of the currency e.g. pence, cents. This is the sum of the base and licence level prices.""",
        alias="total",
    )
    total_uplift: int | None = Field(
        default=None,
        description="""The sum of all uplifts, including licencing, applied to the order in minor units of the currency e.g. pence, cents.""",
        alias="total_uplift",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
