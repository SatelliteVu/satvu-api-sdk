from typing import Union

from pydantic import BaseModel


class ValidationError(BaseModel):
    """
    Attributes:
        loc (list[Union[int, str]]):
        msg (str):
        type (str):
    """

    loc: list[Union[int, str]]
    msg: str
    type: str
