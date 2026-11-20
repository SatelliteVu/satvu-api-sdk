# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

import pydantic

if TYPE_CHECKING:
    from ..models.structured_error import StructuredError


class StructuredErrorResponse(pydantic.BaseModel):
    """An error response with a machine-readable code.

    Attributes:
        error (StructuredError): An error with a machine-readable code, a message, and the values that caused it.
    """

    error: StructuredError = pydantic.Field(
        ...,
        description="""An error with a machine-readable code, a message, and the values that caused it.""",
        alias="error",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
