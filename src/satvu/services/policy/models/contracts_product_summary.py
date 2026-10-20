# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class ContractsProductSummary(pydantic.BaseModel):
    """
    Attributes:
        code (str): Product code Example: PRODUCT.
        currency (str): Product currency Example: GBP.
        assured_tasking_window_days (int | None): Assured tasking window in days. Only present for the ASSURED_PRIORITY
            product. Example: 8.
    """

    code: str = pydantic.Field(..., description="""Product code""", alias="code")
    currency: str = pydantic.Field(
        ..., description="""Product currency""", alias="currency"
    )
    assured_tasking_window_days: int | None = pydantic.Field(
        default=None,
        description="""Assured tasking window in days. Only present for the ASSURED_PRIORITY product.""",
        alias="assured_tasking_window_days",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
