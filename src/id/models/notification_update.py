from typing import Union

from pydantic import BaseModel, Field

from ..models.notification_category import NotificationCategory
from ..models.notification_config import NotificationConfig


class NotificationUpdate(BaseModel):
    """
    Attributes:
        category (Union[None, NotificationCategory]): Category for notification topic
        settings (Union[None, list['NotificationConfig']]): Configuration of notification settings related to a specific
            topic.
    """

    category: Union[None, NotificationCategory] = Field(
        None, description="Category for notification topic"
    )
    settings: Union[None, list["NotificationConfig"]] = Field(
        None,
        description="Configuration of notification settings related to a specific topic.",
    )
