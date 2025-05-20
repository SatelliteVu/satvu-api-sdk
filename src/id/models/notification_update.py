from dataclasses import dataclass
from typing import TYPE_CHECKING, Union

from ..models.notification_category import NotificationCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_config import NotificationConfig


@dataclass
class NotificationUpdate:
    """
    Attributes:
        category (Union[None, NotificationCategory, Unset]): Category for notification topic
        settings (Union[None, Unset, list['NotificationConfig']]): Configuration of notification settings related to a
            specific topic.
    """

    category: Union[None, NotificationCategory, Unset] = UNSET
    settings: Union[None, Unset, list["NotificationConfig"]] = UNSET

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {}
