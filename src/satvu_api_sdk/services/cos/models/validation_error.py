from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ValidationError(BaseModel):
    """
    Attributes:
        loc (list[int | str]):
        msg (str):
        type_ (str):
    """

    loc: list[int | str] = Field(..., description=None, alias="loc")
    msg: str = Field(..., description=None, alias="msg")
    type_: str = Field(..., description=None, alias="type")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
