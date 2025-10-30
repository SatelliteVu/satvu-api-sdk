from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.notification_category import NotificationCategory
from ..models.reseller_notification_category import ResellerNotificationCategory

if TYPE_CHECKING:
    from ..models.notification_settings import NotificationSettings


class VerboseNotification(BaseModel):
    """
    Attributes:
        category (Union['NotificationCategory', 'ResellerNotificationCategory', None]): Category for notification topic
        settings (Union[None, list[NotificationSettings]]): Configuration of notification settings related to a specific
            topic.
    """

    category: Union["NotificationCategory", "ResellerNotificationCategory", None] = (
        Field(None, description="Category for notification topic", alias="category")
    )
    settings: Union[None, list[NotificationSettings]] = Field(
        None,
        description="Configuration of notification settings related to a specific topic.",
        alias="settings",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
