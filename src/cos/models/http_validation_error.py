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
        None, description=None, alias="detail"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
