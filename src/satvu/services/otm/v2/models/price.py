# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class Price(pydantic.BaseModel):
    """
    Attributes:
        currency (str): The currency of the order.
        base (int): The base price of the order in minor units of the currency e.g. pence, cents.
        addon_withhold (int): The price of the order from the chosen withhold option in minor units of the currency e.g.
            pence, cents.
        total (int): The total price of the order in minor units of the currency e.g. pence, cents. This is the sum of
            the base and addon prices.
        total_uplift (int): The sum of all uplifts, including licencing, applied to the order in minor units of the
            currency e.g. pence, cents.
        value (int): Price of the order in minor units of the currency e.g. pence, cents.
        licence_level (int | None): The price of the order from the chosen licence level in minor units of the currency
            e.g. pence, cents.
    """

    currency: str = pydantic.Field(
        ..., description="""The currency of the order.""", alias="currency"
    )
    base: int = pydantic.Field(
        ...,
        description="""The base price of the order in minor units of the currency e.g. pence, cents.""",
        alias="base",
    )
    addon_withhold: int = pydantic.Field(
        ...,
        description="""The price of the order from the chosen withhold option in minor units of the currency e.g. pence, cents.""",
        alias="addon:withhold",
    )
    total: int = pydantic.Field(
        ...,
        description="""The total price of the order in minor units of the currency e.g. pence, cents. This is the sum of the base and addon prices.""",
        alias="total",
    )
    total_uplift: int = pydantic.Field(
        ...,
        description="""The sum of all uplifts, including licencing, applied to the order in minor units of the currency e.g. pence, cents.""",
        alias="total_uplift",
    )
    value: int = pydantic.Field(
        ...,
        description="""Price of the order in minor units of the currency e.g. pence, cents.""",
        alias="value",
    )
    licence_level: int | None = pydantic.Field(
        default=None,
        description="""The price of the order from the chosen licence level in minor units of the currency e.g. pence, cents.""",
        alias="licence_level",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
