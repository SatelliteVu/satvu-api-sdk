# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

if TYPE_CHECKING:
    from ..models.validation_error import ValidationError


class HTTPValidationError(pydantic.BaseModel):
    """
    Attributes:
        detail (Union[None, list[ValidationError]]):
    """

    detail: Union[None, list[ValidationError]] = pydantic.Field(
        default=None, description=None, alias="detail"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
