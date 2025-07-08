from typing import Union
from uuid import UUID

from pydantic import BaseModel


class ResellerSubmissionOrderPayload(BaseModel):
    """
    Attributes:
        item_id (Union[list[str], str]): Item ID.
        reseller_end_user_id (UUID):
        name (Union[None, str]): Optional name of an order
    """

    item_id: Union[list[str], str]
    reseller_end_user_id: UUID
    name: Union[None, str] = None
