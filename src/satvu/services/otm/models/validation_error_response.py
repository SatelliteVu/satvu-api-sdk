# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.validation_error_detail import ValidationErrorDetail


class ValidationErrorResponse(BaseModel):
    """Validation error response for Pydantic validation failures.

    Returned by FastAPI when request validation fails (422 status).
    Contains a list of validation errors with details about each failure.

        Attributes:
            detail (list[ValidationErrorDetail]):
    """

    detail: list[ValidationErrorDetail] = Field(..., description=None, alias="detail")

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
