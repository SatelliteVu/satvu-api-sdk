# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class SeriesPrice(pydantic.BaseModel):
    """Price breakdown for a series, calculated at creation time.

    Attributes:
        currency (str): ISO 4217 currency code.
        base (int): Base price per order in smallest currency unit.
        addon_withhold (int): Withhold addon price per order in smallest currency unit.
        licence_level (int): Licence level addon price per order in smallest currency unit.
        total_price_order (int): Total price per order (base + addons) in smallest currency unit.
        total_uplift_order (int): Total addon uplift per order (addon:withhold + licence_level) in smallest currency
            unit.
        total_order_count (int): Total number of orders in the series.
        total_base_price_series (int): Total base price across all planned orders (base × total_order_count).
        total_uplift_series (int): Total addon uplift across all planned orders (total_uplift_order ×
            total_order_count).
        total_price_series (int): Total price across all planned orders (total_price_order × total_order_count).
    """

    currency: str = pydantic.Field(
        ..., description="""ISO 4217 currency code.""", alias="currency"
    )
    base: int = pydantic.Field(
        ...,
        description="""Base price per order in smallest currency unit.""",
        alias="base",
    )
    addon_withhold: int = pydantic.Field(
        ...,
        description="""Withhold addon price per order in smallest currency unit.""",
        alias="addon:withhold",
    )
    licence_level: int = pydantic.Field(
        ...,
        description="""Licence level addon price per order in smallest currency unit.""",
        alias="licence_level",
    )
    total_price_order: int = pydantic.Field(
        ...,
        description="""Total price per order (base + addons) in smallest currency unit.""",
        alias="total_price_order",
    )
    total_uplift_order: int = pydantic.Field(
        ...,
        description="""Total addon uplift per order (addon:withhold + licence_level) in smallest currency unit.""",
        alias="total_uplift_order",
    )
    total_order_count: int = pydantic.Field(
        ...,
        description="""Total number of orders in the series.""",
        alias="total_order_count",
    )
    total_base_price_series: int = pydantic.Field(
        ...,
        description="""Total base price across all planned orders (base × total_order_count).""",
        alias="total_base_price_series",
    )
    total_uplift_series: int = pydantic.Field(
        ...,
        description="""Total addon uplift across all planned orders (total_uplift_order × total_order_count).""",
        alias="total_uplift_series",
    )
    total_price_series: int = pydantic.Field(
        ...,
        description="""Total price across all planned orders (total_price_order × total_order_count).""",
        alias="total_price_series",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
