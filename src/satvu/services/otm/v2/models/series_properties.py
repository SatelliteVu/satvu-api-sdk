# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING

import pydantic

if TYPE_CHECKING:
    from ..models.series_order_parameters import SeriesOrderParameters


class SeriesProperties(pydantic.BaseModel):
    """Properties for a series creation request.

    Provide either total_order_count or end_date to specify the series length.

        Attributes:
            frequency (str): The recurrence interval, as an ISO 8601 duration (for example, `P7D`, `P14D` or `P1M`). Must
                use whole numbers (for example, `P6M`, not `P0.5Y`) and be at least 7 days.
            start_date (datetime.datetime): When the first order should be created.
            order_parameters (SeriesOrderParameters): The parameters each order in the series is created with.
            name (None | str): The name of the series.
            total_order_count (int | None): Total number of orders to create. Provide either this or end_date.
            end_date (datetime.datetime | None): Optional end date. If provided instead of total_order_count,
                total_order_count is derived as (end_date - start_date) / frequency, rounded up to the nearest whole number.
    """

    frequency: str = pydantic.Field(
        ...,
        description="""The recurrence interval, as an ISO 8601 duration (for example, `P7D`, `P14D` or `P1M`). Must use whole numbers (for example, `P6M`, not `P0.5Y`) and be at least 7 days.""",
        alias="frequency",
    )
    start_date: datetime.datetime = pydantic.Field(
        ...,
        description="""When the first order should be created.""",
        alias="start_date",
    )
    order_parameters: SeriesOrderParameters = pydantic.Field(
        ...,
        description="""The parameters each order in the series is created with.""",
        alias="order_parameters",
    )
    name: None | str = pydantic.Field(
        default=None, description="""The name of the series.""", alias="name"
    )
    total_order_count: int | None = pydantic.Field(
        default=None,
        description="""Total number of orders to create. Provide either this or end_date.""",
        alias="total_order_count",
    )
    end_date: datetime.datetime | None = pydantic.Field(
        default=None,
        description="""Optional end date. If provided instead of total_order_count, total_order_count is derived as (end_date - start_date) / frequency, rounded up to the nearest whole number.""",
        alias="end_date",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
