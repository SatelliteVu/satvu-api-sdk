from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.user_info_deprecated_user_metadata_type_0 import (
        UserInfoDeprecatedUserMetadataType0,
    )


class UserInfoDeprecated(BaseModel):
    """
    Attributes:
        user_id (str):
        name (str):
        email (str):
        user_metadata (Union['UserInfoDeprecatedUserMetadataType0', None]):
        last_login (Union[None, str]):
    """

    user_id: str = Field(..., description=None, alias="user_id")
    name: str = Field(..., description=None, alias="name")
    email: str = Field(..., description=None, alias="email")
    user_metadata: Union["UserInfoDeprecatedUserMetadataType0", None] = Field(
        None, description=None, alias="user_metadata"
    )
    last_login: Union[None, str] = Field(None, description=None, alias="last_login")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
