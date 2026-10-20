# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Any

import pydantic


class ValidationErrorDetail(pydantic.BaseModel):
    """Individual validation error detail from Pydantic.

    Represents a single validation error with location, message, and context.

        Attributes:
            type_ (str):
            loc (list[int | str]):
            msg (str):
            input_ (Any | None):
            ctx (dict | None):
    """

    type_: str = pydantic.Field(..., description=None, alias="type")
    loc: list[int | str] = pydantic.Field(..., description=None, alias="loc")
    msg: str = pydantic.Field(..., description=None, alias="msg")
    input_: Any | None = pydantic.Field(default=None, description=None, alias="input")
    ctx: dict | None = pydantic.Field(default=None, description=None, alias="ctx")

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
