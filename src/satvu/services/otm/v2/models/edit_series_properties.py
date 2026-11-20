# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Union

import pydantic

if TYPE_CHECKING:
    from ..models.edit_series_order_parameters import EditSeriesOrderParameters
    from ..models.point import Point


class EditSeriesProperties(pydantic.BaseModel):
    """Editable fields for series updates.

    Attributes:
        name (None | str): The name of the series.
        geometry (Union['Point', None]): The location of the orders the series creates from now on.
        order_parameters (Union['EditSeriesOrderParameters', None]): Modifications to the parameters of the orders the
            series creates from now on.
        frequency (None | str): The recurrence interval, as an ISO 8601 duration (for example, `P7D`, `P14D` or `P1M`).
            Must use whole numbers (for example, `P6M`, not `P0.5Y`) and be at least 7 days.
        total_order_count (int | None): The total number of orders the series creates. Must be at least
            `orders_created_count`. Send either this or `end_date`.
        end_date (datetime.datetime | None): Updated end date. If provided instead of total_order_count,
            total_order_count is derived as (end_date - start_date) / frequency, rounded up to the nearest whole number.
            Must be after start_date.
    """

    name: None | str = pydantic.Field(
        default=None, description="""The name of the series.""", alias="name"
    )
    geometry: Union[Point, None] = pydantic.Field(
        default=None,
        description="""The location of the orders the series creates from now on.""",
        alias="geometry",
    )
    order_parameters: Union[EditSeriesOrderParameters, None] = pydantic.Field(
        default=None,
        description="""Modifications to the parameters of the orders the series creates from now on.""",
        alias="order_parameters",
    )
    frequency: None | str = pydantic.Field(
        default=None,
        description="""The recurrence interval, as an ISO 8601 duration (for example, `P7D`, `P14D` or `P1M`). Must use whole numbers (for example, `P6M`, not `P0.5Y`) and be at least 7 days.""",
        alias="frequency",
    )
    total_order_count: int | None = pydantic.Field(
        default=None,
        description="""The total number of orders the series creates. Must be at least `orders_created_count`. Send either this or `end_date`.""",
        alias="total_order_count",
    )
    end_date: datetime.datetime | None = pydantic.Field(
        default=None,
        description="""Updated end date. If provided instead of total_order_count, total_order_count is derived as (end_date - start_date) / frequency, rounded up to the nearest whole number. Must be after start_date.""",
        alias="end_date",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
