from typing import TYPE_CHECKING, TypedDict, Union

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_info_deprecated_user_metadata_type_0 import (
        UserInfoDeprecatedUserMetadataType0,
    )


class UserInfoDeprecated(TypedDict):
    """
    Attributes:
        user_id (str):
        name (str):
        email (str):
        user_metadata (Union['UserInfoDeprecatedUserMetadataType0', None, Unset]):
        last_login (Union[None, Unset, str]):
    """

    user_id: str
    name: str
    email: str
    user_metadata: Union["UserInfoDeprecatedUserMetadataType0", None, Unset] = UNSET
    last_login: Union[None, Unset, str] = UNSET
