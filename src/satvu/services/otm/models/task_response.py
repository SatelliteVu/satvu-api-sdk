# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from ..models.user_facing_task_status import UserFacingTaskStatus

if TYPE_CHECKING:
    from ..models.task_acquisition import TaskAcquisition
    from ..models.task_status_history_entry import TaskStatusHistoryEntry


class TaskResponse(BaseModel):
    """A single task assigned to an order.

    Attributes:
        id (UUID): Task ID.
        status ('UserFacingTaskStatus'): User-facing task status values exposed via the API.
        created_at (datetime.datetime): When the task was created.
        updated_at (datetime.datetime): When the task was last updated.
        acquisition (Union['TaskAcquisition', None]): Acquisition metadata.
        status_history (Union[None, list[TaskStatusHistoryEntry]]): Chronological history of status changes, newest
            first.
    """

    id: UUID = Field(..., description="""Task ID.""", alias="id")
    status: UserFacingTaskStatus = Field(
        ...,
        description="""User-facing task status values exposed via the API.""",
        alias="status",
    )
    created_at: datetime.datetime = Field(
        ..., description="""When the task was created.""", alias="created_at"
    )
    updated_at: datetime.datetime = Field(
        ..., description="""When the task was last updated.""", alias="updated_at"
    )
    acquisition: Union[TaskAcquisition, None] = Field(
        default=None, description="""Acquisition metadata.""", alias="acquisition"
    )
    status_history: Union[None, list[TaskStatusHistoryEntry]] = Field(
        default=None,
        description="""Chronological history of status changes, newest first.""",
        alias="status_history",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
