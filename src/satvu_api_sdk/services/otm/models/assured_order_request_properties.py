from __future__ import annotations

from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field


class AssuredOrderRequestProperties(BaseModel):
    """
    Attributes:
        product (Literal['assured']): Assured Priority.
        signature (str): Signature token.
        name (Union[None, str]): The name of the order.
        licence_level (Union[None, str]): The optional licence level for the order Licence levels are specific to the
            contract. If not specified, the option will be set to the licence with the smallest uplift in the relevant
            contract.
        addon_withhold (Union[None, str]): The optional ISO8601 string describing the duration that an order will be
            withheld from the public catalog. Withhold options are specific to the contract. If not specified, the option
            will be set to the default specified in the relevant contract.
    """

    product: Literal["assured"] = Field(
        "assured", description="Assured Priority.", alias="product"
    )
    signature: str = Field(..., description="Signature token.", alias="signature")
    name: Union[None, str] = Field(
        None, description="The name of the order.", alias="name"
    )
    licence_level: Union[None, str] = Field(
        None,
        description="The optional licence level for the order Licence levels are specific to the contract. If not specified, the option will be set to the licence with the smallest uplift in the relevant contract.",
        alias="licence_level",
    )
    addon_withhold: Union[None, str] = Field(
        None,
        description="The optional ISO8601 string describing the duration that an order will be withheld from the public catalog. Withhold options are specific to the contract. If not specified, the option will be set to the default specified in the relevant contract.",
        alias="addon:withhold",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
