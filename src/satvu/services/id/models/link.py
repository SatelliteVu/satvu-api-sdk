# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class Link(pydantic.BaseModel):
    """
    Attributes:
        href (str): The link in the format of a URL.
        rel (str): The relationship between the current document and the linked document.
    """

    href: str = pydantic.Field(
        ..., description="""The link in the format of a URL.""", alias="href"
    )
    rel: str = pydantic.Field(
        ...,
        description="""The relationship between the current document and the linked document.""",
        alias="rel",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
