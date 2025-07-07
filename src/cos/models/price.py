from pydantic import BaseModel


class Price(BaseModel):
    """
    Attributes:
        value (int): The price of the order in minor units of the currency e.g. pence, cents.
        currency (str): The currency of the order.
    """

    value: int
    currency: str
