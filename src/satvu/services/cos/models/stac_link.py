# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class StacLink(pydantic.BaseModel):
    """Related resources and navigation links for the imagery item.

    Attributes:
        href (str):
        rel (str):
        type_ (None | str):
        title (None | str): A human readable title to be used in rendered displays of the link. Default: ''.
    """

    href: str = pydantic.Field(..., description=None, alias="href")
    rel: str = pydantic.Field(..., description=None, alias="rel")
    type_: None | str = pydantic.Field(default=None, description=None, alias="type")
    title: None | str = pydantic.Field(
        default="",
        description="""A human readable title to be used in rendered displays of the link.""",
        alias="title",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
