from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class PriceInformation(BaseModel):
    """Pricing information.

    Attributes:
        currency (str): The currency of the order.
        base (int): The base price of the order in minor units of the currency e.g. pence, cents.
        final (bool): Whether the price is final. When the `baseprice` query parameter is true, this will be false as
            the price may change at order submission time after relevant addons and required licence level have been
            accounted for.
        addon_withhold (int | None): The price of the order from the chosen withhold option in minor units of the
            currency e.g. pence, cents.
        licence_level (int | None): The price of the order from the chosen licence level in minor units of the currency
            e.g. pence, cents.
        total (int | None): The total price of the order in minor units of the currency e.g. pence, cents. This is the
            sum of the base and addon prices.
        total_uplift (int | None): The sum of all uplifts, including licencing, applied to the order in minor units of
            the currency e.g. pence, cents.
        value (int | None): Price of the order in minor units of the currency e.g. pence, cents.
    """

    currency: str = Field(
        ..., description="The currency of the order.", alias="currency"
    )
    base: int = Field(
        ...,
        description="The base price of the order in minor units of the currency e.g. pence, cents.",
        alias="base",
    )
    final: bool = Field(
        ...,
        description="Whether the price is final. When the `baseprice` query parameter is true, this will be false as the price may change at order submission time after relevant addons and required licence level have been accounted for.",
        alias="final",
    )
    addon_withhold: int | None = Field(
        None,
        description="The price of the order from the chosen withhold option in minor units of the currency e.g. pence, cents.",
        alias="addon:withhold",
    )
    licence_level: int | None = Field(
        None,
        description="The price of the order from the chosen licence level in minor units of the currency e.g. pence, cents.",
        alias="licence_level",
    )
    total: int | None = Field(
        None,
        description="The total price of the order in minor units of the currency e.g. pence, cents. This is the sum of the base and addon prices.",
        alias="total",
    )
    total_uplift: int | None = Field(
        None,
        description="The sum of all uplifts, including licencing, applied to the order in minor units of the currency e.g. pence, cents.",
        alias="total_uplift",
    )
    value: int | None = Field(
        None,
        description="Price of the order in minor units of the currency e.g. pence, cents.",
        alias="value",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
