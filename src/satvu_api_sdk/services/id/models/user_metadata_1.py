from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.verbose_notification import VerboseNotification


class UserMetadata1(BaseModel):
    """
    Attributes:
        client_id (None | str): The client ID of the user
        notifications (list[VerboseNotification] | None): The notifications configured for the user.
    """

    client_id: None | str = Field(
        None, description="The client ID of the user", alias="client_id"
    )
    notifications: list[VerboseNotification] | None = Field(
        None,
        description="The notifications configured for the user.",
        alias="notifications",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
