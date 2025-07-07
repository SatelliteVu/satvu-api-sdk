from typing import Union

from pydantic import BaseModel

from ..models.notification_category import NotificationCategory
from ..models.notification_config import NotificationConfig


class NotificationUpdate(BaseModel):
    """
    Attributes:
        category (Union[None, NotificationCategory]): Category for notification topic
        settings (Union[None, list['NotificationConfig']]): Configuration of notification settings related to a specific
            topic.
    """

    category: Union[None, NotificationCategory] = None
    settings: Union[None, list["NotificationConfig"]] = None
