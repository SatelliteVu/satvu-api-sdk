# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class HttpError(pydantic.BaseModel):
    """
    Attributes:
        id (str): A unique identifier for the type of error.
        message (str): An error message describing what went wrong.
    """

    id: str = pydantic.Field(
        ..., description="""A unique identifier for the type of error.""", alias="id"
    )
    message: str = pydantic.Field(
        ...,
        description="""An error message describing what went wrong.""",
        alias="message",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
