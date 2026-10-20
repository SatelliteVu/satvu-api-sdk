# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Literal, Union

import pydantic


class NotificationConfig(pydantic.BaseModel):
    """
    Attributes:
        topic (Literal['tasking:order_status']): Notification topic.
        email (Union[None, bool]): Whether the user has opted into email notifications. Default: False.
    """

    topic: Literal["tasking:order_status"] = pydantic.Field(
        default="tasking:order_status",
        description="""Notification topic.""",
        alias="topic",
    )
    email: Union[None, bool] = pydantic.Field(
        default=False,
        description="""Whether the user has opted into email notifications.""",
        alias="email",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
