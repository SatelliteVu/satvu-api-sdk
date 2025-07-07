from dataclasses import dataclass
from typing import Literal


@dataclass
class AssuredFeasibilityFields:
    """
    Attributes:
        product (Literal['assured']): Assured Priority.
        datetime_ (str): The closed date-time interval of the request.
    """

    product: Literal["assured"]
    datetime_: str

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "product",
            "datetime",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "product": object,
            "datetime": str,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
