from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.user_metadata import UserMetadata


class UserInfo(BaseModel):
    """
    Attributes:
        user_id (str): The ID of the user.
        name (str): The name of the user.
        email (str): The email of the user.
        user_metadata (Union[None, UserMetadata]):
        last_login (None | str): The datetime at which the user last logged in.
    """

    user_id: str = Field(..., description="The ID of the user.", alias="user_id")
    name: str = Field(..., description="The name of the user.", alias="name")
    email: str = Field(..., description="The email of the user.", alias="email")
    user_metadata: Union[None, "UserMetadata"] = Field(
        None, description=None, alias="user_metadata"
    )
    last_login: None | str = Field(
        None,
        description="The datetime at which the user last logged in.",
        alias="last_login",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
