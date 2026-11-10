# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class ErrorResponse(pydantic.BaseModel):
    """Standard error response for custom HTTP exceptions.

    Used when raising HTTPException with a string detail message.

        Attributes:
            detail (str):
    """

    detail: str = pydantic.Field(..., description=None, alias="detail")

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
