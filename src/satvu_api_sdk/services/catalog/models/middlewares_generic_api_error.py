from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.error import Error


class MiddlewaresGenericApiError(BaseModel):
    """
    Attributes:
        errors (Union[None, list[Error]]):
    """

    errors: Union[None, list[Error]] = Field(None, description=None, alias="Errors")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
