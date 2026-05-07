# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class BboxLiteral(BaseModel):
    """
    Attributes:
        bbox (Any):
    """

    bbox: Any = Field(..., description=None, alias="bbox")

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
