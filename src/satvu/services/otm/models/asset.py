# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

import pydantic


class Asset(pydantic.BaseModel):
    """STAC Asset object.

    An Asset is a file associated with a STAC Item that can be downloaded
    or accessed. Each asset has a URI, media type, and semantic roles.

        Attributes:
            href (str): The URI to the asset object.
            type_ (str): The media type of the asset.
            roles (Union[None, list[str]]): The semantic roles of the asset (e.g., 'thumbnail', 'data', 'metadata').
            title (None | str): A human readable title for the asset.
            description (None | str): A description of the asset.
    """

    href: str = pydantic.Field(
        ..., description="""The URI to the asset object.""", alias="href"
    )
    type_: str = pydantic.Field(
        ..., description="""The media type of the asset.""", alias="type"
    )
    roles: Union[None, list[str]] = pydantic.Field(
        default=None,
        description="""The semantic roles of the asset (e.g., 'thumbnail', 'data', 'metadata').""",
        alias="roles",
    )
    title: None | str = pydantic.Field(
        default=None,
        description="""A human readable title for the asset.""",
        alias="title",
    )
    description: None | str = pydantic.Field(
        default=None, description="""A description of the asset.""", alias="description"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
