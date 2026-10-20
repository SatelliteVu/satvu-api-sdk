# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class BatchBalanceResponse(pydantic.BaseModel):
    """Response body for batch credit balance queries.

    Attributes:
        balances (dict): Mapping of contract IDs to their credit balances.
    """

    balances: dict = pydantic.Field(
        ...,
        description="""Mapping of contract IDs to their credit balances.""",
        alias="balances",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
