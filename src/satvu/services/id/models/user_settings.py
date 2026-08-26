# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.notification_update import NotificationUpdate


class UserSettings(BaseModel):
    """
    Attributes:
        notifications (list[NotificationUpdate] | None): Update user notifications settings.A full list of notification
            preferences can be found with the GET user details endpoint. Sending empty or null objects will not modify
            existing preferences.
    """

    notifications: list[NotificationUpdate] | None = Field(
        default=None,
        description="""Update user notifications settings.A full list of notification preferences can be found with the GET user details endpoint. Sending empty or null objects will not modify existing preferences.""",
        alias="notifications",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
