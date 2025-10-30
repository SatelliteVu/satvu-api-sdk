from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class NotificationSettings(BaseModel):
    """
    Attributes:
        topic (str): Notification topic.
        name (str): Name of notification type.
        description (str): Description of notification type.
        email (Union[None, bool]): Opted into email notifications. Default: False.
    """

    topic: str = Field(..., description="Notification topic.", alias="topic")
    name: str = Field(..., description="Name of notification type.", alias="name")
    description: str = Field(
        ..., description="Description of notification type.", alias="description"
    )
    email: Union[None, bool] = Field(
        False, description="Opted into email notifications.", alias="email"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
