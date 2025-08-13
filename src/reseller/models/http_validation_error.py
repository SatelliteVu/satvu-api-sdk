from typing import Union

from pydantic import BaseModel, ConfigDict, Field

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
