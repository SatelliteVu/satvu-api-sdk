# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class NotificationDescription(pydantic.BaseModel):
    """
    Attributes:
        topic (str): Notification topic.
        name (str): Name of notification type.
        description (str): Description of notification type.
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

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
