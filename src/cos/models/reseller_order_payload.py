from dataclasses import dataclass
from typing import Union
from uuid import UUID


@dataclass
class ResellerOrderPayload:
    """
    Attributes:
        item_id (Union[list[str], str]): Item ID.
        reseller_end_user_id (UUID):
    """

    item_id: Union[list[str], str]
    reseller_end_user_id: UUID

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "item_id",
            "reseller_end_user_id",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "item_id": object,
            "reseller_end_user_id": UUID,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
