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
