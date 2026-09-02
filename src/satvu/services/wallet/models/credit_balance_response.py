# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class CreditBalanceResponse(BaseModel):
    """Response body for credit balance queries.

    Attributes:
        currency (str): The currency of the credit balance.
        balance (int): Deprecated: use `credit_available` instead. The credit balance still available to spend, in minor
            currency units (e.g. pence, cents).
        credit_available (int): The credit remaining, and available for use, in minor currency units (e.g. pence,
            cents). Equal to the credit allowance minus `credit_reserved` and `credit_fulfilled`.
        credit_reserved (int): The credit currently reserved for staged/in-progress tasking orders that are not yet
            billable — in minor currency units (e.g. pence, cents).
        credit_fulfilled (int): The total credit redeemed and fully billable, in minor currency units (e.g. pence,
            cents).
        billing_cycle (None | str): The current billing cycle, for example the current calendar month (UTC). If the
            billing cycle is `null`, the billing period will be from the contract start date.
    """

    currency: str = Field(
        ..., description="""The currency of the credit balance.""", alias="currency"
    )
    balance: int = Field(
        ...,
        description="""Deprecated: use `credit_available` instead. The credit balance still available to spend, in minor currency units (e.g. pence, cents).""",
        alias="balance",
    )
    credit_available: int = Field(
        ...,
        description="""The credit remaining, and available for use, in minor currency units (e.g. pence, cents). Equal to the credit allowance minus `credit_reserved` and `credit_fulfilled`.""",
        alias="credit_available",
    )
    credit_reserved: int = Field(
        ...,
        description="""The credit currently reserved for staged/in-progress tasking orders that are not yet billable — in minor currency units (e.g. pence, cents).""",
        alias="credit_reserved",
    )
    credit_fulfilled: int = Field(
        ...,
        description="""The total credit redeemed and fully billable, in minor currency units (e.g. pence, cents).""",
        alias="credit_fulfilled",
    )
    billing_cycle: None | str = Field(
        ...,
        description="""The current billing cycle, for example the current calendar month (UTC). If the billing cycle is `null`, the billing period will be from the contract start date.""",
        alias="billing_cycle",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
