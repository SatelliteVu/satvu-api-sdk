from typing import Union

from pydantic import BaseModel, Field


class OrderEditPayload(BaseModel):
    """
    Attributes:
        name (Union[None, str]): Optional name of an order
    """

    name: Union[None, str] = Field(None, description="Optional name of an order")
