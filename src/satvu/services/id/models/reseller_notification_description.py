# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from ..models.topic import Topic


class ResellerNotificationDescription(BaseModel):
    """
    Attributes:
        topic ('Topic'): Notification topic.
        name (str): Name of notification type.
        description (str): Description of notification type.
    """

    topic: Topic = Field(..., description="""Notification topic.""", alias="topic")
    name: str = Field(..., description="""Name of notification type.""", alias="name")
    description: str = Field(
        ..., description="""Description of notification type.""", alias="description"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
