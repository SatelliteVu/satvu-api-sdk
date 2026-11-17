# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import Any, Literal

import pydantic

from ..models.feasibility_request_status import FeasibilityRequestStatus


class AssuredStoredFeasibilityRequestProperties(pydantic.BaseModel):
    """Properties of the stored assured priority feasibility request.

    Attributes:
        product (Literal['assured']): The tasking product. Always `assured` (Assured tasking).
        datetime_ (str): The tasking window to search for passes in, as an ISO 8601 interval (`start/end`). Both bounds
            are required. The end must not be further in the future than the contract's assured tasking window allows. The
            feasibility response only includes passes from the time of the request onwards.
        status ('FeasibilityRequestStatus'): The status of the feasibility request.
        created_at (datetime.datetime): When the feasibility request was created.
        updated_at (datetime.datetime): When the feasibility request was last updated.
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
    status: FeasibilityRequestStatus = pydantic.Field(
        ..., description="""The status of the feasibility request.""", alias="status"
    )
    created_at: datetime.datetime = pydantic.Field(
        ...,
        description="""When the feasibility request was created.""",
        alias="created_at",
    )
    updated_at: datetime.datetime = pydantic.Field(
        ...,
        description="""When the feasibility request was last updated.""",
        alias="updated_at",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )

    def model_post_init(self, context: Any, /) -> None:
        # Required fields the SDK fills in (constants, spec defaults) must survive
        # model_dump(exclude_unset=True)
        self.__pydantic_fields_set__ = self.model_fields_set.union(["product"])
