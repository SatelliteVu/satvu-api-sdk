from dataclasses import dataclass
from typing import TYPE_CHECKING, Union

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_metadata import UserMetadata


@dataclass
class UserInfo:
    """
    Attributes:
        user_id (str): The ID of the user.
        name (str): The name of the user.
        email (str): The email of the user.
        user_metadata (Union[Unset, UserMetadata]):
        last_login (Union[None, Unset, str]): The datetime at which the user last logged in.
    """

    user_id: str
    name: str
    email: str
    user_metadata: Union[Unset, "UserMetadata"] = UNSET
    last_login: Union[None, Unset, str] = UNSET

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
