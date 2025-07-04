from dataclasses import dataclass
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.user_info_deprecated_user_metadata_type_0 import (
        UserInfoDeprecatedUserMetadataType0,
    )


@dataclass
class UserInfoDeprecated:
    """
    Attributes:
        user_id (str):
        name (str):
        email (str):
        user_metadata (Union['UserInfoDeprecatedUserMetadataType0', None]):
        last_login (Union[None, str]):
    """

    user_id: str
    name: str
    email: str
    user_metadata: Union["UserInfoDeprecatedUserMetadataType0", None] = None
    last_login: Union[None, str] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "user_id",
            "name",
            "email",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "user_id": str,
            "name": str,
            "email": str,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "user_metadata": object,
            "last_login": object,
        }
