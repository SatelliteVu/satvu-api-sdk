from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.reseller_notification_category import ResellerNotificationCategory
from ..models.reseller_notification_config import ResellerNotificationConfig


class ResellerNotificationUpdate(BaseModel):
    """
    Attributes:
        category (Union[None, ResellerNotificationCategory]): Category for notification topic
        settings (Union[None, list[ResellerNotificationConfig]]): Configuration of notification settings related to a
            specific topic.
    """

    category: Union[None, ResellerNotificationCategory] = Field(
        None, description="Category for notification topic", alias="category"
    )
    settings: Union[None, list[ResellerNotificationConfig]] = Field(
        None,
        description="Configuration of notification settings related to a specific topic.",
        alias="settings",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
