from typing import Union

from pydantic import BaseModel, Field


class OrderSubmissionPayload(BaseModel):
    """Request payload for submitting an order.

    Attributes:
        item_id (Union[list[str], str]): The item ID.
        name (Union[None, str]): The optional name of the order
        licence_level (Union[None, str]):
    """

    item_id: Union[list[str], str] = Field(..., description="The item ID.")
    name: Union[None, str] = Field(None, description="The optional name of the order")
    licence_level: Union[None, str] = Field(None, description=None)
