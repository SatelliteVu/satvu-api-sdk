# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class Price(pydantic.BaseModel):
    """
    Attributes:
        currency (str): The currency of the price, as an ISO 4217 code.
        base (int): The base price of the order. In minor units of the currency (for example, pence or cents).
        addon_withhold (int): The uplift from the chosen withhold option. In minor units of the currency (for example,
            pence or cents).
        total (int): The total price of the order: the base price plus all uplifts. In minor units of the currency (for
            example, pence or cents).
        total_uplift (int): The sum of all uplifts applied to the order, including the licence level. In minor units of
            the currency (for example, pence or cents).
        value (int): The price of the order. In minor units of the currency (for example, pence or cents).
        licence_level (int | None): The uplift from the chosen licence level. In minor units of the currency (for
            example, pence or cents).
    """

    currency: str = pydantic.Field(
        ...,
        description="""The currency of the price, as an ISO 4217 code.""",
        alias="currency",
    )
    base: int = pydantic.Field(
        ...,
        description="""The base price of the order. In minor units of the currency (for example, pence or cents).""",
        alias="base",
    )
    addon_withhold: int = pydantic.Field(
        ...,
        description="""The uplift from the chosen withhold option. In minor units of the currency (for example, pence or cents).""",
        alias="addon:withhold",
    )
    total: int = pydantic.Field(
        ...,
        description="""The total price of the order: the base price plus all uplifts. In minor units of the currency (for example, pence or cents).""",
        alias="total",
    )
    total_uplift: int = pydantic.Field(
        ...,
        description="""The sum of all uplifts applied to the order, including the licence level. In minor units of the currency (for example, pence or cents).""",
        alias="total_uplift",
    )
    value: int = pydantic.Field(
        ...,
        description="""The price of the order. In minor units of the currency (for example, pence or cents).""",
        alias="value",
    )
    licence_level: int | None = pydantic.Field(
        default=None,
        description="""The uplift from the chosen licence level. In minor units of the currency (for example, pence or cents).""",
        alias="licence_level",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
