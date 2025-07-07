from typing import Union

from pydantic import BaseModel

from ..models.validation_error import ValidationError


class HTTPValidationError(BaseModel):
    """
    Attributes:
        detail (Union[None, list['ValidationError']]):
    """

    detail: Union[None, list["ValidationError"]] = None

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
            "detail": object,
        }
