from dataclasses import dataclass
from typing import Union


@dataclass
class CreditBalanceResponse:
    """
    Attributes:
        currency (str): The currency of the credit balance.
        balance (int): The credit balance of the user, in minor units of the currency e.g. pence, cents.
        billing_cycle (Union[None, str]): The current billing cycle, for example the current calendar month (UTC). If
            the billing cycle is None, the billing period will be from the contract start date.
    """

    currency: str
    balance: int
    billing_cycle: Union[None, str]

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "currency",
            "balance",
            "billing_cycle",
        }
