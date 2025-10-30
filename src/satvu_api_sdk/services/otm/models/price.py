from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class Price(BaseModel):
    """
    Attributes:
        value (Union[None, int]): Price of the order in minor units of the currency e.g. pence, cents.
        currency (Union[None, str]): The currency of the order.
    """

    value: Union[None, int] = Field(
        None,
        description="Price of the order in minor units of the currency e.g. pence, cents.",
        alias="value",
    )
    currency: Union[None, str] = Field(
        None, description="The currency of the order.", alias="currency"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
