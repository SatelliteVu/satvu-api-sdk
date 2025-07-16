from pydantic import BaseModel, Field


class Price(BaseModel):
    """
    Attributes:
        value (int): The price of the order in minor units of the currency e.g. pence, cents.
        currency (str): The currency of the order.
    """

    value: int = Field(
        ...,
        description="The price of the order in minor units of the currency e.g. pence, cents.",
    )
    currency: str = Field(..., description="The currency of the order.")
