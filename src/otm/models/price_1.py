from pydantic import BaseModel, ConfigDict, Field


class Price1(BaseModel):
    """
    Attributes:
        currency (str): The currency of the order.
        base (int): The base price of the order in minor units of the currency e.g. pence, cents.
        addon_withhold (int): The price of the order from the chosen withhold option in minor units of the currency e.g.
            pence, cents.
        total (int): The total price of the order in minor units of the currency e.g. pence, cents. This is the sum of
            the base and addon prices.
        value (int): Price of the order in minor units of the currency e.g. pence, cents.
    """

    currency: str = Field(
        ..., description="The currency of the order.", alias="currency"
    )
    base: int = Field(
        ...,
        description="The base price of the order in minor units of the currency e.g. pence, cents.",
        alias="base",
    )
    addon_withhold: int = Field(
        ...,
        description="The price of the order from the chosen withhold option in minor units of the currency e.g. pence, cents.",
        alias="addon:withhold",
    )
    total: int = Field(
        ...,
        description="The total price of the order in minor units of the currency e.g. pence, cents. This is the sum of the base and addon prices.",
        alias="total",
    )
    value: int = Field(
        ...,
        description="Price of the order in minor units of the currency e.g. pence, cents.",
        alias="value",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
