# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class CreditBalanceResponse(BaseModel):
    """Response body for credit balance queries.

    Attributes:
        currency (str): The currency of the credit balance.
        balance (int): The credit balance of the user in minor currency units (e.g. pence, cents).
        billing_cycle (None | str): The current billing cycle, for example the current calendar month (UTC). If the
            billing cycle is `null`, the billing period will be from the contract start date.
    """

    currency: str = Field(
        ..., description="""The currency of the credit balance.""", alias="currency"
    )
    balance: int = Field(
        ...,
        description="""The credit balance of the user in minor currency units (e.g. pence, cents).""",
        alias="balance",
    )
    billing_cycle: None | str = Field(
        ...,
        description="""The current billing cycle, for example the current calendar month (UTC). If the billing cycle is `null`, the billing period will be from the contract start date.""",
        alias="billing_cycle",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
