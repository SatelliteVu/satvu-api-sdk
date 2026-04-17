# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.validation_error_detail import ValidationErrorDetail


class UnprocessableResponse(BaseModel):
    """
    Attributes:
        detail (list[ValidationErrorDetail] | str):
    """

    detail: list[ValidationErrorDetail] | str = Field(
        ..., description=None, alias="detail"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
