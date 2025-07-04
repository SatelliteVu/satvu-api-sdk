from dataclasses import dataclass
from typing import Union


@dataclass
class CivilDate:
    """Contract end date

    Attributes:
        day (Union[None, int]):
        month (Union[None, int]):
        year (Union[None, int]):
    """

    day: Union[None, int] = None
    month: Union[None, int] = None
    year: Union[None, int] = None

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
            "Day": int,
            "Month": int,
            "Year": int,
        }
