from typing import Union

from pydantic import BaseModel, Field

from ..models.user_info_deprecated_user_metadata_type_0 import (
    UserInfoDeprecatedUserMetadataType0,
)


class UserInfoDeprecated(BaseModel):
    """
    Attributes:
        user_id (str):
        name (str):
        email (str):
        user_metadata (Union[None, UserInfoDeprecatedUserMetadataType0]):
        last_login (Union[None, str]):
    """

    user_id: str = Field(..., description=None)
    name: str = Field(..., description=None)
    email: str = Field(..., description=None)
    user_metadata: Union[None, UserInfoDeprecatedUserMetadataType0] = Field(
        None, description=None
    )
    last_login: Union[None, str] = Field(None, description=None)
