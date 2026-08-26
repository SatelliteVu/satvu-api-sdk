# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.notification_category import NotificationCategory

if TYPE_CHECKING:
    from ..models.notification_settings import NotificationSettings


class VerboseNotification(BaseModel):
    """
    Attributes:
        category (Union['NotificationCategory', None]): Category for notification topic
        settings (list[NotificationSettings] | None): Configuration of notification settings related to a specific
            topic.
    """

    category: Union[NotificationCategory, None] = Field(
        default=None,
        description="""Category for notification topic""",
        alias="category",
    )
    settings: list[NotificationSettings] | None = Field(
        default=None,
        description="""Configuration of notification settings related to a specific topic.""",
        alias="settings",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
