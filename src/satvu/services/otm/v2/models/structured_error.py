# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class StructuredError(pydantic.BaseModel):
    """An error with a machine-readable code, a message, and the values that caused it.

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
