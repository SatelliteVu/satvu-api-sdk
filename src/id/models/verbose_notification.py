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
