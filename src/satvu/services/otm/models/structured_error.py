# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class StructuredError(BaseModel):
    """Machine-readable error body carrying a code, message, and context.

    Used for validation failures where the frontend needs the specific values
    (requested vs. required) to render actionable feedback, rather than
    string-parsing a free-text message.

        Attributes:
            code (str):
            message (str):
            details (dict):
    """

    code: str = Field(..., description=None, alias="code")
    message: str = Field(..., description=None, alias="message")
    details: dict = Field(..., description=None, alias="details")

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
