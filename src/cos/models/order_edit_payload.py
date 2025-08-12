from typing import Union

from pydantic import BaseModel, Field


class OrderEditPayload(BaseModel):
    """Request payload for editing an order.

    Attributes:
        name (Union[None, str]): The optional name of the order
    """

    name: Union[None, str] = Field(None, description="The optional name of the order")
