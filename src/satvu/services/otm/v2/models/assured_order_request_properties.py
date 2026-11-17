# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Any, Literal

import pydantic


class AssuredOrderRequestProperties(pydantic.BaseModel):
    """
    Attributes:
        product (Literal['assured']): The tasking product. Always `assured` (Assured tasking).
        signature (str): The signature token from an assured feasibility response.
        name (None | str): The name of the order.
        licence_level (None | str): The licence level for the order. Licence levels are specific to the contract.
            Defaults to the contract's licence level with the smallest uplift.
        addon_withhold (None | str): How long the order's imagery is withheld from the public catalog, as an ISO 8601
            duration. Withhold options are specific to the contract. Defaults to the contract's default withhold option.
    """

    product: Literal["assured"] = pydantic.Field(
        default="assured",
        description="""The tasking product. Always `assured` (Assured tasking).""",
        alias="product",
    )
    signature: str = pydantic.Field(
        ...,
        description="""The signature token from an assured feasibility response.""",
        alias="signature",
    )
    name: None | str = pydantic.Field(
        default=None, description="""The name of the order.""", alias="name"
    )
    licence_level: None | str = pydantic.Field(
        default=None,
        description="""The licence level for the order. Licence levels are specific to the contract. Defaults to the contract's licence level with the smallest uplift.""",
        alias="licence_level",
    )
    addon_withhold: None | str = pydantic.Field(
        default=None,
        description="""How long the order's imagery is withheld from the public catalog, as an ISO 8601 duration. Withhold options are specific to the contract. Defaults to the contract's default withhold option.""",
        alias="addon:withhold",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )

    def model_post_init(self, context: Any, /) -> None:
        # Required fields the SDK fills in (constants, spec defaults) must survive
        # model_dump(exclude_unset=True)
        self.__pydantic_fields_set__ = self.model_fields_set.union(["product"])
