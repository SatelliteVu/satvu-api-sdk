from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class Price(BaseModel):
    """Pricing information.

    Attributes:
        value (int): The price of the order in minor units of the currency e.g. pence, cents.
        currency (str): The currency of the order.
    """

    value: int = Field(
        ...,
        description="The price of the order in minor units of the currency e.g. pence, cents.",
        alias="value",
    )
    currency: str = Field(
        ..., description="The currency of the order.", alias="currency"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
