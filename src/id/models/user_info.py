from typing import Union

from pydantic import BaseModel, Field

from ..models.user_metadata import UserMetadata


class UserInfo(BaseModel):
    """
    Attributes:
        user_id (str): The ID of the user.
        name (str): The name of the user.
        email (str): The email of the user.
        user_metadata (Union[None, UserMetadata]):
        last_login (Union[None, str]): The datetime at which the user last logged in.
    """

    user_id: str = Field(..., description="The ID of the user.")
    name: str = Field(..., description="The name of the user.")
    email: str = Field(..., description="The email of the user.")
    user_metadata: Union[None, "UserMetadata"] = Field(None, description=None)
    last_login: Union[None, str] = Field(
        None, description="The datetime at which the user last logged in."
    )
