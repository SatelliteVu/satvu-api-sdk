from dataclasses import dataclass
from typing import Union


@dataclass
class TermsUserTermsAccepted:
    """
    Attributes:
        accepted (Union[None, bool]):
        user_id (Union[None, str]):
    """

    accepted: Union[None, bool] = None
    user_id: Union[None, str] = None

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
            "accepted": bool,
            "user_id": str,
        }
