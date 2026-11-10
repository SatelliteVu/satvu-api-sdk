# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class StructuredError(pydantic.BaseModel):
    """Machine-readable error body carrying a code, message, and context.

    Used for validation failures where the frontend needs the specific values
    (requested vs. required) to render actionable feedback, rather than
    string-parsing a free-text message.

        Attributes:
            code (str):
            message (str):
            details (dict):
    """

    code: str = pydantic.Field(..., description=None, alias="code")
    message: str = pydantic.Field(..., description=None, alias="message")
    details: dict = pydantic.Field(..., description=None, alias="details")

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
