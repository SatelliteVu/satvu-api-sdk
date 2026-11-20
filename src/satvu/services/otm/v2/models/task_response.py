# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Union
from uuid import UUID

import pydantic

from ..models.user_facing_task_status import UserFacingTaskStatus

if TYPE_CHECKING:
    from ..models.task_acquisition import TaskAcquisition
    from ..models.task_status_history_entry import TaskStatusHistoryEntry


class TaskResponse(pydantic.BaseModel):
    """A task: one attempt to acquire an order.

    Attributes:
        id (UUID): The ID of the task.
        status ('UserFacingTaskStatus'): The status of a task.
        created_at (datetime.datetime): When the task was created.
        updated_at (datetime.datetime): When the task was last updated.
        acquisition (Union['TaskAcquisition', None]): Acquisition metadata.
        status_history (Union[None, list[TaskStatusHistoryEntry]]): Chronological history of status changes, newest
            first.
    """

    id: UUID = pydantic.Field(..., description="""The ID of the task.""", alias="id")
    status: UserFacingTaskStatus = pydantic.Field(
        ..., description="""The status of a task.""", alias="status"
    )
    created_at: datetime.datetime = pydantic.Field(
        ..., description="""When the task was created.""", alias="created_at"
    )
    updated_at: datetime.datetime = pydantic.Field(
        ..., description="""When the task was last updated.""", alias="updated_at"
    )
    acquisition: Union[TaskAcquisition, None] = pydantic.Field(
        default=None, description="""Acquisition metadata.""", alias="acquisition"
    )
    status_history: Union[None, list[TaskStatusHistoryEntry]] = pydantic.Field(
        default=None,
        description="""Chronological history of status changes, newest first.""",
        alias="status_history",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
