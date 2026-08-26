# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.point import Point
    from ..models.series_order_parameters import SeriesOrderParameters


class EditSeriesProperties(BaseModel):
    """Editable fields for series updates.

    Attributes:
        name (None | str): Optional human-readable label.
        geometry (Union['Point', None]): Updated target location for future child orders.
        order_parameters (Union['SeriesOrderParameters', None]): Updated template for future child orders.
        frequency (None | str): Updated ISO 8601 recurrence interval (e.g. P7D, P14D, P1M).
        total_order_count (int | None): Updated total planned orders (must be >= orders_created_count). Provide either
            this or end_date.
        end_date (datetime.datetime | None): Updated end date. If provided instead of total_order_count,
            total_order_count is derived as (end_date - start_date) / frequency, rounded up to the nearest whole number.
            Must be after start_date.
    """

    name: None | str = Field(
        default=None, description="""Optional human-readable label.""", alias="name"
    )
    geometry: Union[Point, None] = Field(
        default=None,
        description="""Updated target location for future child orders.""",
        alias="geometry",
    )
    order_parameters: Union[SeriesOrderParameters, None] = Field(
        default=None,
        description="""Updated template for future child orders.""",
        alias="order_parameters",
    )
    frequency: None | str = Field(
        default=None,
        description="""Updated ISO 8601 recurrence interval (e.g. P7D, P14D, P1M).""",
        alias="frequency",
    )
    total_order_count: int | None = Field(
        default=None,
        description="""Updated total planned orders (must be >= orders_created_count). Provide either this or end_date.""",
        alias="total_order_count",
    )
    end_date: datetime.datetime | None = Field(
        default=None,
        description="""Updated end date. If provided instead of total_order_count, total_order_count is derived as (end_date - start_date) / frequency, rounded up to the nearest whole number. Must be after start_date.""",
        alias="end_date",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
