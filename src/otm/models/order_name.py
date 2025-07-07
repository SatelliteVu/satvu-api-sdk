from typing import Union

from pydantic import BaseModel


class OrderName(BaseModel):
    """
    Attributes:
        name (Union[None, str]): The name of the order.
    """

    name: Union[None, str] = None
