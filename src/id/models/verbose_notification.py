from typing import Union

from pydantic import BaseModel

from ..models.notification_category import NotificationCategory
from ..models.notification_settings import NotificationSettings


class VerboseNotification(BaseModel):
    """
    Attributes:
        category (Union[None, NotificationCategory]): Category for notification topic
        settings (Union[None, list['NotificationSettings']]): Configuration of notification settings related to a
            specific topic.
    """

    category: Union[None, NotificationCategory] = None
    settings: Union[None, list["NotificationSettings"]] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {}

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {}

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "category": object,
            "settings": object,
        }
