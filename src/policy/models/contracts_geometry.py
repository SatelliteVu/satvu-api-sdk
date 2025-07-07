from typing import Any, Union

from pydantic import BaseModel


class ContractsGeometry(BaseModel):
    """Allowed geographical area of the contract

    Attributes:
        coordinates (Union[None, Any]): Value of any type, including null
        type (Union[None, str]):
    """

    coordinates: Union[None, Any] = None
    type: Union[None, str] = None

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
            "coordinates": object,
            "type": str,
        }
