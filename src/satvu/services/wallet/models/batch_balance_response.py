# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class BatchBalanceResponse(BaseModel):
    """Response body for batch credit balance queries.

    Attributes:
        balances (dict): Mapping of contract IDs to their credit balances.
    """

    balances: dict = Field(
        ...,
        description="""Mapping of contract IDs to their credit balances.""",
        alias="balances",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
