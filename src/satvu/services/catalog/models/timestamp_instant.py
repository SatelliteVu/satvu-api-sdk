# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class TimestampInstant(BaseModel):
    """
    Attributes:
        timestamp (str):
    """

    timestamp: str = Field(..., description=None, alias="timestamp")

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
