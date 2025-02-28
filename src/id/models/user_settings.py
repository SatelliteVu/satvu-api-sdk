from typing import TYPE_CHECKING, TypedDict, Union

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_update import NotificationUpdate


class UserSettings(TypedDict):
    """
    Attributes:
        notifications (Union[None, Unset, list['NotificationUpdate']]): Update user notifications settings.A full list
            of notification preferences can be found with the GET user details endpoint. Sending empty or null objects will
            not modify existing preferences.
    """

    notifications: Union[None, Unset, list["NotificationUpdate"]] = UNSET
