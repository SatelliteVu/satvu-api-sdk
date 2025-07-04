from dataclasses import dataclass
from typing import Any, Union


@dataclass
class RouterQueryResult:
    """
    Attributes:
        message (Union[None, str]):
        result (Union[None, Any]): Value of any type, including null
    """

    message: Union[None, str] = None
    result: Union[None, Any] = None

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
            "message": str,
            "result": object,
        }
