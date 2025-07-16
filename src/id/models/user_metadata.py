from typing import Union

from pydantic import BaseModel, Field

from ..models.verbose_notification import VerboseNotification


class UserMetadata(BaseModel):
    """
    Attributes:
        client_id (Union[None, str]): The client ID of the user
        notifications (Union[None, list['VerboseNotification']]): The notifications configured for the user.
    """

    client_id: Union[None, str] = Field(None, description="The client ID of the user")
    notifications: Union[None, list["VerboseNotification"]] = Field(
        None, description="The notifications configured for the user."
    )
