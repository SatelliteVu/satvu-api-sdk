# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

import pydantic


class Error(pydantic.BaseModel):
    """
    Attributes:
        id (str): A unique identifier for the type of error.
        message (str): An error message describing what went wrong.
        field (Union[None, str]): The field that failed validation, for 'ValidationError' errors only.
    """

    id: str = pydantic.Field(
        ..., description="""A unique identifier for the type of error.""", alias="id"
    )
    message: str = pydantic.Field(
        ...,
        description="""An error message describing what went wrong.""",
        alias="message",
    )
    field: Union[None, str] = pydantic.Field(
        default=None,
        description="""The field that failed validation, for 'ValidationError' errors only.""",
        alias="field",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
