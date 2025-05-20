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
