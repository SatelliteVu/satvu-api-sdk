# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.order_status import OrderStatus


class StatusHistoryEntry(BaseModel):
    """A single status transition in the order's lifecycle.

    Attributes:
        status_to ('OrderStatus'):
        datetime_updated (datetime.datetime): When the status transition occurred.
        reason (str): Reason for the status change.
        status_from (Union['OrderStatus', None]): Previous status before transition (null for initial order creation).
    """

    status_to: OrderStatus = Field(..., description=None, alias="status_to")
    datetime_updated: datetime.datetime = Field(
        ...,
        description="""When the status transition occurred.""",
        alias="datetime_updated",
    )
    reason: str = Field(
        ..., description="""Reason for the status change.""", alias="reason"
    )
    status_from: Union[OrderStatus, None] = Field(
        default=None,
        description="""Previous status before transition (null for initial order creation).""",
        alias="status_from",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
