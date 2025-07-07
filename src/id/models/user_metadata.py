from typing import Union

from pydantic import BaseModel

from ..models.verbose_notification import VerboseNotification


class UserMetadata(BaseModel):
    """
    Attributes:
        client_id (Union[None, str]): The client ID of the user
        notifications (Union[None, list['VerboseNotification']]): The notifications configured for the user.
    """

    client_id: Union[None, str] = None
    notifications: Union[None, list["VerboseNotification"]] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {}

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {}

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "client_id": object,
            "notifications": object,
        }
