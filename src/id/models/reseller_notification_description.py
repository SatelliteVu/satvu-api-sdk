from pydantic import BaseModel, Field

from ..models.reseller_notification_description_topic import (
    ResellerNotificationDescriptionTopic,
)


class ResellerNotificationDescription(BaseModel):
    """
    Attributes:
        topic (ResellerNotificationDescriptionTopic): Notification topic.
        name (str): Name of notification type.
        description (str): Description of notification type.
    """

    topic: ResellerNotificationDescriptionTopic = Field(
        ..., description="Notification topic."
    )
    name: str = Field(..., description="Name of notification type.")
    description: str = Field(..., description="Description of notification type.")
