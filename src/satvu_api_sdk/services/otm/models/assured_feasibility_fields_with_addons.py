from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class AssuredFeasibilityFieldsWithAddons(BaseModel):
    """
    Attributes:
        product (Literal['assured']): Assured Priority.
        datetime_ (str): The closed date-time interval of the request.
        licence_level (None | str): The optional licence level for the order. Licence levels are specific to the
            contract.
        addon_withhold (None | str): The optional ISO8601 string describing the duration that an order will be withheld
            from the public catalog. Withhold options are specific to the contract.
    """

    product: Literal["assured"] = Field(
        "assured", description="Assured Priority.", alias="product"
    )
    datetime_: str = Field(
        ...,
        description="The closed date-time interval of the request.",
        alias="datetime",
    )
    licence_level: None | str = Field(
        None,
        description="The optional licence level for the order. Licence levels are specific to the contract.",
        alias="licence_level",
    )
    addon_withhold: None | str = Field(
        None,
        description="The optional ISO8601 string describing the duration that an order will be withheld from the public catalog. Withhold options are specific to the contract.",
        alias="addon:withhold",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
