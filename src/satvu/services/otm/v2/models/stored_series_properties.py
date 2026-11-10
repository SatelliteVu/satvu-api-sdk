# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING
from uuid import UUID

import pydantic

if TYPE_CHECKING:
    from ..models.stored_series_order_parameters import StoredSeriesOrderParameters


class StoredSeriesProperties(pydantic.BaseModel):
    """Properties returned in a series response.

    Attributes:
        id (UUID): Series UUID.
        created_at (datetime.datetime): The datetime at which the series was created.
        updated_at (datetime.datetime): The datetime at which the series was last updated.
        owned_by (str): User who created the series.
        contract_id (UUID): Contract ID.
        status (str): Series status.
        frequency (str): ISO 8601 recurrence interval.
        start_date (datetime.datetime): When the first order is scheduled.
        total_order_count (int): Total planned orders.
        orders_created_count (int): Orders created so far.
        order_parameters (StoredSeriesOrderParameters): Order parameters as stored on a series and returned in
            responses.

            Extends the request parameters with `product`, which is set server-side
            (always ``standard``) rather than provided by the requester.
        name (None | str): Optional human-readable label for this series.
        next_window (None | str): Datetime interval of the next scheduled order window (ISO 8601 interval, e.g.
            '2026-06-01T00:00:00Z/2026-06-15T00:00:00Z'). Null when all orders have been created.
        reseller_end_user_id (None | UUID): End user UUID for reseller series.
    """

    id: UUID = pydantic.Field(..., description="""Series UUID.""", alias="id")
    created_at: datetime.datetime = pydantic.Field(
        ...,
        description="""The datetime at which the series was created.""",
        alias="created_at",
    )
    updated_at: datetime.datetime = pydantic.Field(
        ...,
        description="""The datetime at which the series was last updated.""",
        alias="updated_at",
    )
    owned_by: str = pydantic.Field(
        ..., description="""User who created the series.""", alias="owned_by"
    )
    contract_id: UUID = pydantic.Field(
        ..., description="""Contract ID.""", alias="contract_id"
    )
    status: str = pydantic.Field(..., description="""Series status.""", alias="status")
    frequency: str = pydantic.Field(
        ..., description="""ISO 8601 recurrence interval.""", alias="frequency"
    )
    start_date: datetime.datetime = pydantic.Field(
        ..., description="""When the first order is scheduled.""", alias="start_date"
    )
    total_order_count: int = pydantic.Field(
        ..., description="""Total planned orders.""", alias="total_order_count"
    )
    orders_created_count: int = pydantic.Field(
        ..., description="""Orders created so far.""", alias="orders_created_count"
    )
    order_parameters: StoredSeriesOrderParameters = pydantic.Field(
        ...,
        description="""Order parameters as stored on a series and returned in responses.

Extends the request parameters with `product`, which is set server-side
(always ``standard``) rather than provided by the requester.""",
        alias="order_parameters",
    )
    name: None | str = pydantic.Field(
        default=None,
        description="""Optional human-readable label for this series.""",
        alias="name",
    )
    next_window: None | str = pydantic.Field(
        default=None,
        description="""Datetime interval of the next scheduled order window (ISO 8601 interval, e.g. '2026-06-01T00:00:00Z/2026-06-15T00:00:00Z'). Null when all orders have been created.""",
        alias="next_window",
    )
    reseller_end_user_id: None | UUID = pydantic.Field(
        default=None,
        description="""End user UUID for reseller series.""",
        alias="reseller_end_user_id",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
