from typing import TYPE_CHECKING, TypedDict, Union

from ..models.notification_category import NotificationCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_config import NotificationConfig


class NotificationUpdate(TypedDict):
    """
    Attributes:
        category (Union[None, NotificationCategory, Unset]): Category for notification topic
        settings (Union[None, Unset, list['NotificationConfig']]): Configuration of notification settings related to a
            specific topic.
    """

    category: Union[None, NotificationCategory, Unset] = UNSET
    settings: Union[None, Unset, list["NotificationConfig"]] = UNSET
