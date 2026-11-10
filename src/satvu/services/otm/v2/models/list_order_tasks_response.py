# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pydantic

if TYPE_CHECKING:
    from ..models.task_response import TaskResponse


class ListOrderTasksResponse(pydantic.BaseModel):
    """Response for listing all tasks for an order.

    Attributes:
        order_id (UUID): The order these tasks belong to.
        tasks (list[TaskResponse]): Tasks sorted by creation date, newest first.
    """

    order_id: UUID = pydantic.Field(
        ..., description="""The order these tasks belong to.""", alias="order_id"
    )
    tasks: list[TaskResponse] = pydantic.Field(
        ...,
        description="""Tasks sorted by creation date, newest first.""",
        alias="tasks",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
