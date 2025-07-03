from dataclasses import dataclass
from typing import TYPE_CHECKING, Union

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.verbose_notification import VerboseNotification


@dataclass
class UserMetadata:
    """
    Attributes:
        client_id (Union[None, Unset, str]): The client ID of the user
        notifications (Union[None, Unset, list['VerboseNotification']]): The notifications configured for the user.
    """

    client_id: Union[None, Unset, str] = UNSET
    notifications: Union[None, Unset, list["VerboseNotification"]] = UNSET

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
