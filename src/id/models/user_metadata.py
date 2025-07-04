from dataclasses import dataclass
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.verbose_notification import VerboseNotification


@dataclass
class UserMetadata:
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
