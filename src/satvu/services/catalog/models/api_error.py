# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

import pydantic

if TYPE_CHECKING:
    from ..models.error import Error


class ApiError(pydantic.BaseModel):
    """
    Attributes:
        errors (list[Error]):
    """

    errors: list[Error] = pydantic.Field(..., description=None, alias="errors")

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
