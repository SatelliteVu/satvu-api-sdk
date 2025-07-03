from dataclasses import dataclass
from typing import TYPE_CHECKING, Union

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validation_error import ValidationError


@dataclass
class HTTPValidationError:
    """
    Attributes:
        detail (Union[Unset, list['ValidationError']]):
    """

    detail: Union[Unset, list["ValidationError"]] = UNSET

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
