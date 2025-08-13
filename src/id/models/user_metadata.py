from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.verbose_notification import VerboseNotification


class UserMetadata(BaseModel):
    """
    Attributes:
        client_id (Union[None, str]): The client ID of the user
        notifications (Union[None, list[VerboseNotification]]): The notifications configured for the user.
    """

    client_id: Union[None, str] = Field(
        None, description="The client ID of the user", alias="client_id"
    )
    notifications: Union[None, list[VerboseNotification]] = Field(
        None,
        description="The notifications configured for the user.",
        alias="notifications",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
