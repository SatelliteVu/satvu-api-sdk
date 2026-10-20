# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

import pydantic

if TYPE_CHECKING:
    from ..models.validation_error_detail import ValidationErrorDetail


class ValidationErrorResponse(pydantic.BaseModel):
    """Validation error response for Pydantic validation failures.

    Returned by FastAPI when request validation fails (422 status).
    Contains a list of validation errors with details about each failure.

        Attributes:
            detail (list[ValidationErrorDetail]):
    """

    detail: list[ValidationErrorDetail] = pydantic.Field(
        ..., description=None, alias="detail"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
