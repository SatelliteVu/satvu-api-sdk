from dataclasses import dataclass
from typing import Union


@dataclass
class OrderPayload:
    """
    Attributes:
        item_id (Union[list[str], str]): Item ID.
    """

    item_id: Union[list[str], str]

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "item_id",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "item_id": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
