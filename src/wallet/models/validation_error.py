from typing import Union

from pydantic import BaseModel, Field


class ValidationError(BaseModel):
    """
    Attributes:
        loc (list[Union[int, str]]):
        msg (str):
        type (str):
    """

    loc: list[Union[int, str]] = Field(..., description=None)
    msg: str = Field(..., description=None)
    type: str = Field(..., description=None)
