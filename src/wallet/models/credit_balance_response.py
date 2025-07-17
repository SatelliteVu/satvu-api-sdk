from typing import Union

from pydantic import BaseModel, Field


class CreditBalanceResponse(BaseModel):
    """
    Attributes:
        currency (str): The currency of the credit balance.
        balance (int): The credit balance of the user, in minor units of the currency e.g. pence, cents.
        billing_cycle (Union[None, str]): The current billing cycle, for example the current calendar month (UTC). If
            the billing cycle is None, the billing period will be from the contract start date.
    """

    currency: str = Field(..., description="The currency of the credit balance.")
    balance: int = Field(
        ...,
        description="The credit balance of the user, in minor units of the currency e.g. pence, cents.",
    )
    billing_cycle: Union[None, str] = Field(
        ...,
        description="The current billing cycle, for example the current calendar month (UTC). If the billing cycle is None, the billing period will be from the contract start date.",
    )
