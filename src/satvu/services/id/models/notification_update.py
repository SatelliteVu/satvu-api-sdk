# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

from ..models.notification_category import NotificationCategory

if TYPE_CHECKING:
    from ..models.notification_config import NotificationConfig


class NotificationUpdate(pydantic.BaseModel):
    """
    Attributes:
        category (Union['NotificationCategory', None]): Category for notification topic
        settings (list[NotificationConfig] | None): Configuration of notification settings related to a specific topic.
    """

    category: Union[NotificationCategory, None] = pydantic.Field(
        default=None,
        description="""Category for notification topic""",
        alias="category",
    )
    settings: list[NotificationConfig] | None = pydantic.Field(
        default=None,
        description="""Configuration of notification settings related to a specific topic.""",
        alias="settings",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
