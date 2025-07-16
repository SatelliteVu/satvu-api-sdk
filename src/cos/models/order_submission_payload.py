from typing import Union

from pydantic import BaseModel, Field


class OrderSubmissionPayload(BaseModel):
    """
    Attributes:
        item_id (Union[list[str], str]): Item ID.
        name (Union[None, str]): Optional name of an order
    """

    item_id: Union[list[str], str] = Field(..., description="Item ID.")
    name: Union[None, str] = Field(None, description="Optional name of an order")
