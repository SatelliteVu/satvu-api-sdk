from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.notification_category import NotificationCategory
from ..models.notification_config import NotificationConfig


class NotificationUpdate(BaseModel):
    """
    Attributes:
        category (Union[None, NotificationCategory]): Category for notification topic
        settings (Union[None, list[NotificationConfig]]): Configuration of notification settings related to a specific
            topic.
    """

    category: Union[None, NotificationCategory] = Field(
        None, description="Category for notification topic", alias="category"
    )
    settings: Union[None, list[NotificationConfig]] = Field(
        None,
        description="Configuration of notification settings related to a specific topic.",
        alias="settings",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
