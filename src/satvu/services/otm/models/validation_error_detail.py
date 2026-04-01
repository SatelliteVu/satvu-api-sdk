# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class ValidationErrorDetail(BaseModel):
    """Individual validation error detail from Pydantic.

    Represents a single validation error with location, message, and context.

        Attributes:
            type_ (str):
            loc (list[int | str]):
            msg (str):
            input_ (Any | None):
            ctx (dict | None):
    """

    type_: str = Field(..., description=None, alias="type")
    loc: list[int | str] = Field(..., description=None, alias="loc")
    msg: str = Field(..., description=None, alias="msg")
    input_: Any | None = Field(default=None, description=None, alias="input")
    ctx: dict | None = Field(default=None, description=None, alias="ctx")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
