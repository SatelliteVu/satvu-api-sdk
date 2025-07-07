from pydantic import BaseModel

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

    topic: ResellerNotificationDescriptionTopic
    name: str
    description: str
