# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import Union

import pydantic

from ..models.user_facing_task_status import UserFacingTaskStatus


class TaskStatusHistoryEntry(pydantic.BaseModel):
    """A single status transition in the task's lifecycle.

    Attributes:
        status_to ('UserFacingTaskStatus'): User-facing task status values exposed via the API.
        datetime_updated (datetime.datetime): When the status transition occurred.
        reason (str): Reason for the status change.
        status_from (Union['UserFacingTaskStatus', None]): Previous status before transition (null for initial
            assignment).
        details (None | str): Additional context about the status change.
    """

    status_to: UserFacingTaskStatus = pydantic.Field(
        ...,
        description="""User-facing task status values exposed via the API.""",
        alias="status_to",
    )
    datetime_updated: datetime.datetime = pydantic.Field(
        ...,
        description="""When the status transition occurred.""",
        alias="datetime_updated",
    )
    reason: str = pydantic.Field(
        ..., description="""Reason for the status change.""", alias="reason"
    )
    status_from: Union[UserFacingTaskStatus, None] = pydantic.Field(
        default=None,
        description="""Previous status before transition (null for initial assignment).""",
        alias="status_from",
    )
    details: None | str = pydantic.Field(
        default=None,
        description="""Additional context about the status change.""",
        alias="details",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
