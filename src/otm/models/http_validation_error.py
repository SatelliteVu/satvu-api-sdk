from typing import Union

from pydantic import BaseModel, Field

from ..models.validation_error import ValidationError


class HTTPValidationError(BaseModel):
    """
    Attributes:
        detail (Union[None, list['ValidationError']]):
    """

    detail: Union[None, list["ValidationError"]] = Field(None, description=None)
