from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.notification_update import NotificationUpdate


class UserSettings(BaseModel):
    """
    Attributes:
        notifications (Union[None, list[NotificationUpdate]]): Update user notifications settings.A full list of
            notification preferences can be found with the GET user details endpoint. Sending empty or null objects will not
            modify existing preferences.
    """

    notifications: Union[None, list[NotificationUpdate]] = Field(
        None,
        description="Update user notifications settings.A full list of notification preferences can be found with the GET user details endpoint. Sending empty or null objects will not modify existing preferences.",
        alias="notifications",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
