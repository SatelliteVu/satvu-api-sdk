# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.topic import Topic


class ResellerNotificationConfig(BaseModel):
    """
    Attributes:
        topic ('Topic'): Notification topic.
        email (Union[None, bool]): Whether the user has opted into email notifications. Default: False.
    """

    topic: Topic = Field(..., description="""Notification topic.""", alias="topic")
    email: Union[None, bool] = Field(
        default=False,
        description="""Whether the user has opted into email notifications.""",
        alias="email",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
