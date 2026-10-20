# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

import pydantic

if TYPE_CHECKING:
    from ..models.verbose_notification import VerboseNotification


class UserMetadata(pydantic.BaseModel):
    """
    Attributes:
        client_id (None | str): The client ID of the user
        notifications (list[VerboseNotification] | None): The notifications configured for the user.
    """

    client_id: None | str = pydantic.Field(
        default=None, description="""The client ID of the user""", alias="client_id"
    )
    notifications: list[VerboseNotification] | None = pydantic.Field(
        default=None,
        description="""The notifications configured for the user.""",
        alias="notifications",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
