# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class PriceInformation(pydantic.BaseModel):
    """Pricing information.

    Attributes:
        currency (str): The currency of the price, as an ISO 4217 code.
        base (int): The base price of the order. In minor units of the currency (for example, pence or cents).
        final (bool): Whether the price is final. When the `baseprice` query parameter is true, this will be false as
            the price may change at order submission time after relevant addons and required licence level have been
            accounted for.
        addon_withhold (int | None): The uplift from the chosen withhold option. In minor units of the currency (for
            example, pence or cents).
        licence_level (int | None): The uplift from the chosen licence level. In minor units of the currency (for
            example, pence or cents).
        total (int | None): The total price of the order: the base price plus all uplifts. In minor units of the
            currency (for example, pence or cents).
        total_uplift (int | None): The sum of all uplifts applied to the order, including the licence level. In minor
            units of the currency (for example, pence or cents).
        value (int | None): The price of the order. In minor units of the currency (for example, pence or cents).
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
    final: bool = pydantic.Field(
        ...,
        description="""Whether the price is final. When the `baseprice` query parameter is true, this will be false as the price may change at order submission time after relevant addons and required licence level have been accounted for.""",
        alias="final",
    )
    addon_withhold: int | None = pydantic.Field(
        default=None,
        description="""The uplift from the chosen withhold option. In minor units of the currency (for example, pence or cents).""",
        alias="addon:withhold",
    )
    licence_level: int | None = pydantic.Field(
        default=None,
        description="""The uplift from the chosen licence level. In minor units of the currency (for example, pence or cents).""",
        alias="licence_level",
    )
    total: int | None = pydantic.Field(
        default=None,
        description="""The total price of the order: the base price plus all uplifts. In minor units of the currency (for example, pence or cents).""",
        alias="total",
    )
    total_uplift: int | None = pydantic.Field(
        default=None,
        description="""The sum of all uplifts applied to the order, including the licence level. In minor units of the currency (for example, pence or cents).""",
        alias="total_uplift",
    )
    value: int | None = pydantic.Field(
        default=None,
        description="""The price of the order. In minor units of the currency (for example, pence or cents).""",
        alias="value",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
