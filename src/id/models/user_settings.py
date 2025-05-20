from dataclasses import dataclass
from typing import TYPE_CHECKING, Union

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_update import NotificationUpdate


@dataclass
class UserSettings:
    """
    Attributes:
        notifications (Union[None, Unset, list['NotificationUpdate']]): Update user notifications settings.A full list
            of notification preferences can be found with the GET user details endpoint. Sending empty or null objects will
            not modify existing preferences.
    """

    notifications: Union[None, Unset, list["NotificationUpdate"]] = UNSET

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {}
