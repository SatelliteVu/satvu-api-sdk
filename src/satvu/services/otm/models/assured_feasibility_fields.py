# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class AssuredFeasibilityFields(BaseModel):
    """
    Attributes:
        product (Literal['assured']): Assured Priority.
        datetime_ (str): The closed date-time interval of the request, measured from the time the request is made. The
            upper bound must not extend further into the future than the contract's assured tasking window; feasibility
            results only include passes from the request time onwards.
    """

    product: Literal["assured"] = Field(
        default="assured", description="""Assured Priority.""", alias="product"
    )
    datetime_: str = Field(
        ...,
        description="""The closed date-time interval of the request, measured from the time the request is made. The upper bound must not extend further into the future than the contract's assured tasking window; feasibility results only include passes from the request time onwards.""",
        alias="datetime",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
