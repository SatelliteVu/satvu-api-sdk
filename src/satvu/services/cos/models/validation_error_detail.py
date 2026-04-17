# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ValidationErrorDetail(BaseModel):
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
