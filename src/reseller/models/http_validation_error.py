from typing import Union

from pydantic import BaseModel

from ..models.validation_error import ValidationError


class HTTPValidationError(BaseModel):
    """
    Attributes:
        detail (Union[None, list['ValidationError']]):
    """

    detail: Union[None, list["ValidationError"]] = None
