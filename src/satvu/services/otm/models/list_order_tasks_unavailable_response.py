# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ListOrderTasksUnavailableResponse(BaseModel):
    """Response when task information is not available.

    Attributes:
        order_id (UUID): The order ID.
        tasks (Union[None, None]):
        message (Union[None, str]): Explanation of why tasks are unavailable. Default: 'Tasking information is not
            available for this order.'.
    """

    order_id: UUID = Field(..., description="""The order ID.""", alias="order_id")
    tasks: Union[None, None] = Field(default=None, description=None, alias="tasks")
    message: Union[None, str] = Field(
        default="Tasking information is not available for this order.",
        description="""Explanation of why tasks are unavailable.""",
        alias="message",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
