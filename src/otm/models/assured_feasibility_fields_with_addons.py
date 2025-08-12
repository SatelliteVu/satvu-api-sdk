from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field


class AssuredFeasibilityFieldsWithAddons(BaseModel):
    """
    Attributes:
        product (Literal['assured']): Assured Priority.
        datetime_ (str): The closed date-time interval of the request.
        addon_withhold (Union[None, str]): Optional ISO8601 string describing the duration that an order will be
            withheld from the public catalog. Withhold options are specific to the contract. If not specified, the option
            will be set to the default specified in the relevant contract.
    """

    product: Literal["assured"] = Field(
        "assured", description="Assured Priority.", alias="product"
    )
    datetime_: str = Field(
        ...,
        description="The closed date-time interval of the request.",
        alias="datetime",
    )
    addon_withhold: Union[None, str] = Field(
        None,
        description="Optional ISO8601 string describing the duration that an order will be withheld from the public catalog. Withhold options are specific to the contract. If not specified, the option will be set to the default specified in the relevant contract.",
        alias="addon:withhold",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
