# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Any, Union

from pydantic import BaseModel, ConfigDict, Field


class ValidationError(BaseModel):
    """
    Attributes:
        loc (list[int | str]):
        msg (str):
        type_ (str):
        input_ (Union[None, Any]):
        ctx (Union[None, dict]):
    """

    loc: list[int | str] = Field(..., description=None, alias="loc")
    msg: str = Field(..., description=None, alias="msg")
    type_: str = Field(..., description=None, alias="type")
    input_: Union[None, Any] = Field(default=None, description=None, alias="input")
    ctx: Union[None, dict] = Field(default=None, description=None, alias="ctx")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
