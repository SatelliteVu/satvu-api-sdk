from typing import Union

from pydantic import BaseModel

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

    user_id: str
    name: str
    email: str
    user_metadata: Union[None, "UserMetadata"] = None
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
