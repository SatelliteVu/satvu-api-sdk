# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class Link1(pydantic.BaseModel):
    """STAC Link object.

    Links are used to express relationships between STAC objects
    (Items, Collections, Catalogs).

        Attributes:
            href (str): The URL to the linked resource.
            rel (str): The relationship type (e.g., 'self', 'root', 'parent', 'collection').
            type_ (None | str): The media type of the linked resource.
            title (None | str): A human readable title to be used in rendered displays of the link.
    """

    href: str = pydantic.Field(
        ..., description="""The URL to the linked resource.""", alias="href"
    )
    rel: str = pydantic.Field(
        ...,
        description="""The relationship type (e.g., 'self', 'root', 'parent', 'collection').""",
        alias="rel",
    )
    type_: None | str = pydantic.Field(
        default=None,
        description="""The media type of the linked resource.""",
        alias="type",
    )
    title: None | str = pydantic.Field(
        default=None,
        description="""A human readable title to be used in rendered displays of the link.""",
        alias="title",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
