from typing import Union
from uuid import UUID

from pydantic import BaseModel, Field


class ResellerSubmissionOrderPayload(BaseModel):
    """
    Attributes:
        item_id (Union[list[str], str]): Item ID.
        reseller_end_user_id (UUID):
        name (Union[None, str]): Optional name of an order
    """

    item_id: Union[list[str], str] = Field(..., description="Item ID.")
    reseller_end_user_id: UUID = Field(..., description=None)
    name: Union[None, str] = Field(None, description="Optional name of an order")
