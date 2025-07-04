from dataclasses import dataclass
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.notification_update import NotificationUpdate


@dataclass
class UserSettings:
    """
    Attributes:
        notifications (Union[None, list['NotificationUpdate']]): Update user notifications settings.A full list of
            notification preferences can be found with the GET user details endpoint. Sending empty or null objects will not
            modify existing preferences.
    """

    notifications: Union[None, list["NotificationUpdate"]] = None

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
            "notifications": object,
        }
