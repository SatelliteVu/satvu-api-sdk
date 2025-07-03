from dataclasses import dataclass
from typing import Union


@dataclass
class ValidationError:
    """
    Attributes:
        loc (list[Union[int, str]]):
        msg (str):
        type (str):
    """

    loc: list[Union[int, str]]
    msg: str
    type: str

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "loc",
            "msg",
            "type",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "loc": object,
            "msg": str,
            "type": str,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
