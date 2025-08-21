from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.http_error import HttpError


class MiddlewaresApiError(BaseModel):
    """
    Attributes:
        errors (list[HttpError]):
    """

    errors: list[HttpError] = Field(..., description=None, alias="errors")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
