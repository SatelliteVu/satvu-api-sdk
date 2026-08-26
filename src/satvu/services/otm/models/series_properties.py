# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.series_order_parameters import SeriesOrderParameters


class SeriesProperties(BaseModel):
    """Properties for a series creation request.

    Provide either total_order_count or end_date to specify the series length.

        Attributes:
            frequency (str): ISO 8601 duration string for the recurrence interval (e.g. P7D, P14D, P1M). Minimum 7 days.
            start_date (datetime.datetime): When the first order should be created.
            order_parameters (SeriesOrderParameters): Template parameters applied to each child order in the series.
            name (None | str): Optional human-readable label for this series.
            total_order_count (int | None): Total number of orders to create. Provide either this or end_date.
            end_date (datetime.datetime | None): Optional end date. If provided instead of total_order_count,
                total_order_count is derived as (end_date - start_date) / frequency, rounded up to the nearest whole number.
    """

    frequency: str = Field(
        ...,
        description="""ISO 8601 duration string for the recurrence interval (e.g. P7D, P14D, P1M). Minimum 7 days.""",
        alias="frequency",
    )
    start_date: datetime.datetime = Field(
        ...,
        description="""When the first order should be created.""",
        alias="start_date",
    )
    order_parameters: SeriesOrderParameters = Field(
        ...,
        description="""Template parameters applied to each child order in the series.""",
        alias="order_parameters",
    )
    name: None | str = Field(
        default=None,
        description="""Optional human-readable label for this series.""",
        alias="name",
    )
    total_order_count: int | None = Field(
        default=None,
        description="""Total number of orders to create. Provide either this or end_date.""",
        alias="total_order_count",
    )
    end_date: datetime.datetime | None = Field(
        default=None,
        description="""Optional end date. If provided instead of total_order_count, total_order_count is derived as (end_date - start_date) / frequency, rounded up to the nearest whole number.""",
        alias="end_date",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
