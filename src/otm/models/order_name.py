from typing import Union

from pydantic import BaseModel, Field


class OrderName(BaseModel):
    """
    Attributes:
        name (Union[None, str]): The name of the order.
    """

    name: Union[None, str] = Field(None, description="The name of the order.")
