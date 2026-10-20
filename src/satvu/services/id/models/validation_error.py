# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Any, Union

import pydantic


class ValidationError(pydantic.BaseModel):
    """
    Attributes:
        loc (list[int | str]):
        msg (str):
        type_ (str):
        input_ (Union[None, Any]):
        ctx (Union[None, dict]):
    """

    loc: list[int | str] = pydantic.Field(..., description=None, alias="loc")
    msg: str = pydantic.Field(..., description=None, alias="msg")
    type_: str = pydantic.Field(..., description=None, alias="type")
    input_: Union[None, Any] = pydantic.Field(
        default=None, description=None, alias="input"
    )
    ctx: Union[None, dict] = pydantic.Field(default=None, description=None, alias="ctx")

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
