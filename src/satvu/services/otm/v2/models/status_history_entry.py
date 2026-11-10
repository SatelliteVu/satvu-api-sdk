# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import Union

import pydantic

from ..models.order_status import OrderStatus


class StatusHistoryEntry(pydantic.BaseModel):
    """A single status transition in the order's lifecycle.

    Attributes:
        status_to ('OrderStatus'):
        datetime_updated (datetime.datetime): When the status transition occurred.
        reason (str): Reason for the status change.
        status_from (Union['OrderStatus', None]): Previous status before transition (null for initial order creation).
    """

    status_to: OrderStatus = pydantic.Field(..., description=None, alias="status_to")
    datetime_updated: datetime.datetime = pydantic.Field(
        ...,
        description="""When the status transition occurred.""",
        alias="datetime_updated",
    )
    reason: str = pydantic.Field(
        ..., description="""Reason for the status change.""", alias="reason"
    )
    status_from: Union[OrderStatus, None] = pydantic.Field(
        default=None,
        description="""Previous status before transition (null for initial order creation).""",
        alias="status_from",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
