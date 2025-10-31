from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.notification_update import NotificationUpdate
    from ..models.reseller_notification_update import ResellerNotificationUpdate


class UserSettings(BaseModel):
    """
    Attributes:
        notifications (list[NotificationUpdate] | list[ResellerNotificationUpdate] | None): Update user notifications
            settings.A full list of notification preferences can be found with the GET user details endpoint. Sending empty
            or null objects will not modify existing preferences.
    """

    notifications: (
        list[NotificationUpdate] | list[ResellerNotificationUpdate] | None
    ) = Field(
        None,
        description="Update user notifications settings.A full list of notification preferences can be found with the GET user details endpoint. Sending empty or null objects will not modify existing preferences.",
        alias="notifications",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
