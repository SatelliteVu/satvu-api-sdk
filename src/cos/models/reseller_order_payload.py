from typing import TypedDict, Union
from uuid import UUID


class ResellerOrderPayload(TypedDict):
    """
    Attributes:
        item_id (Union[list[str], str]): Item ID.
        reseller_end_user_id (UUID):
    """

    item_id: Union[list[str], str]
    reseller_end_user_id: UUID
