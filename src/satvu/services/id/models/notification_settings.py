# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

import pydantic


class NotificationSettings(pydantic.BaseModel):
    """
    Attributes:
        topic (str): Notification topic.
        name (str): Name of notification type.
        description (str): Description of notification type.
        email (Union[None, bool]): Whether the user has opted into email notifications. Default: False.
    """

    topic: str = pydantic.Field(
        ..., description="""Notification topic.""", alias="topic"
    )
    name: str = pydantic.Field(
        ..., description="""Name of notification type.""", alias="name"
    )
    description: str = pydantic.Field(
        ..., description="""Description of notification type.""", alias="description"
    )
    email: Union[None, bool] = pydantic.Field(
        default=False,
        description="""Whether the user has opted into email notifications.""",
        alias="email",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
