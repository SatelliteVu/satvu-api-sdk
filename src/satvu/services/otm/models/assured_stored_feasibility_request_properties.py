# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from ..models.feasibility_request_status import FeasibilityRequestStatus


class AssuredStoredFeasibilityRequestProperties(BaseModel):
    """Properties of the stored assured priority feasibility request.

    Attributes:
        product (Literal['assured']): Assured Priority.
        datetime_ (str): The closed date-time interval of the request, measured from the time the request is made. The
            upper bound must not extend further into the future than the contract's assured tasking window; feasibility
            results only include passes from the request time onwards.
        status ('FeasibilityRequestStatus'): The status of the feasibility request.
        created_at (datetime.datetime): The datetime at which the feasibility request was created.
        updated_at (datetime.datetime): The datetime at which the feasibility request was last updated.
    """

    product: Literal["assured"] = Field(
        default="assured", description="""Assured Priority.""", alias="product"
    )
    datetime_: str = Field(
        ...,
        description="""The closed date-time interval of the request, measured from the time the request is made. The upper bound must not extend further into the future than the contract's assured tasking window; feasibility results only include passes from the request time onwards.""",
        alias="datetime",
    )
    status: FeasibilityRequestStatus = Field(
        ..., description="""The status of the feasibility request.""", alias="status"
    )
    created_at: datetime.datetime = Field(
        ...,
        description="""The datetime at which the feasibility request was created.""",
        alias="created_at",
    )
    updated_at: datetime.datetime = Field(
        ...,
        description="""The datetime at which the feasibility request was last updated.""",
        alias="updated_at",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
