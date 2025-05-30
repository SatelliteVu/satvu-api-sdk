from dataclasses import dataclass

from ..models.reseller_notification_description_topic import (
    ResellerNotificationDescriptionTopic,
)


@dataclass
class ResellerNotificationDescription:
    """
    Attributes:
        topic (ResellerNotificationDescriptionTopic): Notification topic.
        name (str): Name of notification type.
        description (str): Description of notification type.
    """

    topic: ResellerNotificationDescriptionTopic
    name: str
    description: str

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "topic",
            "name",
            "description",
        }
