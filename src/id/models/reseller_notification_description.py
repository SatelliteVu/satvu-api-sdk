from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from ..models.reseller_notification_description_topic import (
    ResellerNotificationDescriptionTopic,
)


class ResellerNotificationDescription(BaseModel):
    """
    Attributes:
        topic ('ResellerNotificationDescriptionTopic'): Notification topic.
        name (str): Name of notification type.
        description (str): Description of notification type.
    """

    topic: "ResellerNotificationDescriptionTopic" = Field(
        ..., description="Notification topic.", alias="topic"
    )
    name: str = Field(..., description="Name of notification type.", alias="name")
    description: str = Field(
        ..., description="Description of notification type.", alias="description"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
