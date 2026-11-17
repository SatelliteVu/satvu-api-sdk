# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class SeriesPrice(pydantic.BaseModel):
    """Price breakdown for a series, calculated at creation time.

    Attributes:
        currency (str): The currency of the price, as an ISO 4217 code.
        base (int): The base price of each order. In minor units of the currency (for example, pence or cents).
        addon_withhold (int): The uplift from the chosen withhold option on each order. In minor units of the currency
            (for example, pence or cents).
        licence_level (int): The uplift from the chosen licence level on each order. In minor units of the currency (for
            example, pence or cents).
        total_price_order (int): The total price of each order: the base price plus all uplifts. In minor units of the
            currency (for example, pence or cents).
        total_uplift_order (int): The sum of all uplifts on each order. In minor units of the currency (for example,
            pence or cents).
        total_order_count (int): Total number of orders in the series.
        total_base_price_series (int): The base price across every order in the series: `base` multiplied by
            `total_order_count`. In minor units of the currency (for example, pence or cents).
        total_uplift_series (int): The sum of all uplifts across every order in the series: `total_uplift_order`
            multiplied by `total_order_count`. In minor units of the currency (for example, pence or cents).
        total_price_series (int): The total price across every order in the series: `total_price_order` multiplied by
            `total_order_count`. In minor units of the currency (for example, pence or cents).
    """

    currency: str = pydantic.Field(
        ...,
        description="""The currency of the price, as an ISO 4217 code.""",
        alias="currency",
    )
    base: int = pydantic.Field(
        ...,
        description="""The base price of each order. In minor units of the currency (for example, pence or cents).""",
        alias="base",
    )
    addon_withhold: int = pydantic.Field(
        ...,
        description="""The uplift from the chosen withhold option on each order. In minor units of the currency (for example, pence or cents).""",
        alias="addon:withhold",
    )
    licence_level: int = pydantic.Field(
        ...,
        description="""The uplift from the chosen licence level on each order. In minor units of the currency (for example, pence or cents).""",
        alias="licence_level",
    )
    total_price_order: int = pydantic.Field(
        ...,
        description="""The total price of each order: the base price plus all uplifts. In minor units of the currency (for example, pence or cents).""",
        alias="total_price_order",
    )
    total_uplift_order: int = pydantic.Field(
        ...,
        description="""The sum of all uplifts on each order. In minor units of the currency (for example, pence or cents).""",
        alias="total_uplift_order",
    )
    total_order_count: int = pydantic.Field(
        ...,
        description="""Total number of orders in the series.""",
        alias="total_order_count",
    )
    total_base_price_series: int = pydantic.Field(
        ...,
        description="""The base price across every order in the series: `base` multiplied by `total_order_count`. In minor units of the currency (for example, pence or cents).""",
        alias="total_base_price_series",
    )
    total_uplift_series: int = pydantic.Field(
        ...,
        description="""The sum of all uplifts across every order in the series: `total_uplift_order` multiplied by `total_order_count`. In minor units of the currency (for example, pence or cents).""",
        alias="total_uplift_series",
    )
    total_price_series: int = pydantic.Field(
        ...,
        description="""The total price across every order in the series: `total_price_order` multiplied by `total_order_count`. In minor units of the currency (for example, pence or cents).""",
        alias="total_price_series",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
