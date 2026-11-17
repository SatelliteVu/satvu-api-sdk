# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Any, Literal

import pydantic


class AssuredFeasibilityFieldsWithAddons(pydantic.BaseModel):
    """
    Attributes:
        product (Literal['assured']): The tasking product. Always `assured` (Assured tasking).
        datetime_ (str): The tasking window to search for passes in, as an ISO 8601 interval (`start/end`). Both bounds
            are required. The end must not be further in the future than the contract's assured tasking window allows. The
            feasibility response only includes passes from the time of the request onwards.
        licence_level (None | str): The licence level for the order. Licence levels are specific to the contract.
        addon_withhold (None | str): How long the order's imagery is withheld from the public catalog, as an ISO 8601
            duration. Withhold options are specific to the contract.
    """

    product: Literal["assured"] = pydantic.Field(
        default="assured",
        description="""The tasking product. Always `assured` (Assured tasking).""",
        alias="product",
    )
    datetime_: str = pydantic.Field(
        ...,
        description="""The tasking window to search for passes in, as an ISO 8601 interval (`start/end`). Both bounds are required. The end must not be further in the future than the contract's assured tasking window allows. The feasibility response only includes passes from the time of the request onwards.""",
        alias="datetime",
    )
    licence_level: None | str = pydantic.Field(
        default=None,
        description="""The licence level for the order. Licence levels are specific to the contract.""",
        alias="licence_level",
    )
    addon_withhold: None | str = pydantic.Field(
        default=None,
        description="""How long the order's imagery is withheld from the public catalog, as an ISO 8601 duration. Withhold options are specific to the contract.""",
        alias="addon:withhold",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )

    def model_post_init(self, context: Any, /) -> None:
        # Required fields the SDK fills in (constants, spec defaults) must survive
        # model_dump(exclude_unset=True)
        self.__pydantic_fields_set__ = self.model_fields_set.union(["product"])
