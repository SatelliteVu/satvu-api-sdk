from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class Price(BaseModel):
    """
    Attributes:
        value (int | None): Price of the order in minor units of the currency e.g. pence, cents.
        currency (None | str): The currency of the order.
    """

    value: int | None = Field(
        None,
        description="Price of the order in minor units of the currency e.g. pence, cents.",
        alias="value",
    )
    currency: None | str = Field(
        None, description="The currency of the order.", alias="currency"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
