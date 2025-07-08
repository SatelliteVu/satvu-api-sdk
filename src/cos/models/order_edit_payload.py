from typing import Union

from pydantic import BaseModel


class OrderEditPayload(BaseModel):
    """
    Attributes:
        name (Union[None, str]): Optional name of an order
    """

    name: Union[None, str] = None
