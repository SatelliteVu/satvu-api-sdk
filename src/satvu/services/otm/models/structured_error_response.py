# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.structured_error import StructuredError


class StructuredErrorResponse(BaseModel):
    """Response envelope wrapping a :class:`StructuredError`.

    Attributes:
        error (StructuredError): Machine-readable error body carrying a code, message, and context.

            Used for validation failures where the frontend needs the specific values
            (requested vs. required) to render actionable feedback, rather than
            string-parsing a free-text message.
    """

    error: StructuredError = Field(
        ...,
        description="""Machine-readable error body carrying a code, message, and context.

Used for validation failures where the frontend needs the specific values
(requested vs. required) to render actionable feedback, rather than
string-parsing a free-text message.""",
        alias="error",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
