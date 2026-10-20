# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Literal

import pydantic


class AssuredOrderRequestProperties(pydantic.BaseModel):
    """
    Attributes:
        product (Literal['assured']): Assured Priority.
        signature (str): Signature token.
        name (None | str): The name of the order.
        licence_level (None | str): The optional licence level for the order. Licence levels are specific to the
            contract. If not specified, the option will be set to the licence with the smallest uplift in the relevant
            contract.
        addon_withhold (None | str): The optional ISO8601 string describing the duration that an order will be withheld
            from the public catalog. Withhold options are specific to the contract. If not specified, the option will be set
            to the default specified in the relevant contract.
    """

    product: Literal["assured"] = pydantic.Field(
        default="assured", description="""Assured Priority.""", alias="product"
    )
    signature: str = pydantic.Field(
        ..., description="""Signature token.""", alias="signature"
    )
    name: None | str = pydantic.Field(
        default=None, description="""The name of the order.""", alias="name"
    )
    licence_level: None | str = pydantic.Field(
        default=None,
        description="""The optional licence level for the order. Licence levels are specific to the contract. If not specified, the option will be set to the licence with the smallest uplift in the relevant contract.""",
        alias="licence_level",
    )
    addon_withhold: None | str = pydantic.Field(
        default=None,
        description="""The optional ISO8601 string describing the duration that an order will be withheld from the public catalog. Withhold options are specific to the contract. If not specified, the option will be set to the default specified in the relevant contract.""",
        alias="addon:withhold",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
