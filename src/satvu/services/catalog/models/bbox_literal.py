# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Any

import pydantic


class BboxLiteral(pydantic.BaseModel):
    """
    Attributes:
        bbox (Any):
    """

    bbox: Any = pydantic.Field(..., description=None, alias="bbox")

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
