from dataclasses import dataclass
from typing import Union


@dataclass
class Price:
    """
    Attributes:
        value (Union[None, int]): Price of the order in minor units of the currency e.g. pence, cents.
        currency (Union[None, str]): The currency of the order.
    """

    value: Union[None, int] = None
    currency: Union[None, str] = None

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
            "value": object,
            "currency": object,
        }
