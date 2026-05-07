# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.validation_error import ValidationError


class HTTPValidationError(BaseModel):
    """
    Attributes:
        detail (Union[None, list[ValidationError]]):
    """

    detail: Union[None, list[ValidationError]] = Field(
        default=None, description=None, alias="detail"
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
