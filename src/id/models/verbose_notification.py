from dataclasses import dataclass
from typing import TYPE_CHECKING, Union

from ..models.notification_category import NotificationCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_settings import NotificationSettings


@dataclass
class VerboseNotification:
    """
    Attributes:
        category (Union[None, NotificationCategory, Unset]): Category for notification topic
        settings (Union[None, Unset, list['NotificationSettings']]): Configuration of notification settings related to a
            specific topic.
    """

    category: Union[None, NotificationCategory, Unset] = UNSET
    settings: Union[None, Unset, list["NotificationSettings"]] = UNSET

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
