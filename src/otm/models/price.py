from typing import Union

from pydantic import BaseModel


class Price(BaseModel):
    """
    Attributes:
        value (Union[None, int]): Price of the order in minor units of the currency e.g. pence, cents.
        currency (Union[None, str]): The currency of the order.
    """

    value: Union[None, int] = None
    currency: Union[None, str] = None
