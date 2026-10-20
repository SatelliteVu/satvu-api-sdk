# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class TimestampInstant(pydantic.BaseModel):
    """
    Attributes:
        timestamp (str):
    """

    timestamp: str = pydantic.Field(..., description=None, alias="timestamp")

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
