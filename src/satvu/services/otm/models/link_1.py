# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class Link1(BaseModel):
    """STAC Link object.

    Links are used to express relationships between STAC objects
    (Items, Collections, Catalogs).

        Attributes:
            href (str): The URL to the linked resource.
            rel (str): The relationship type (e.g., 'self', 'root', 'parent', 'collection').
            type_ (None | str): The media type of the linked resource.
            title (None | str): A human readable title to be used in rendered displays of the link.
    """

    href: str = Field(
        ..., description="""The URL to the linked resource.""", alias="href"
    )
    rel: str = Field(
        ...,
        description="""The relationship type (e.g., 'self', 'root', 'parent', 'collection').""",
        alias="rel",
    )
    type_: None | str = Field(
        default=None,
        description="""The media type of the linked resource.""",
        alias="type",
    )
    title: None | str = Field(
        default=None,
        description="""A human readable title to be used in rendered displays of the link.""",
        alias="title",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
