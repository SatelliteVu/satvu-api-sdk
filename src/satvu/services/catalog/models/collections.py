# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

import pydantic

if TYPE_CHECKING:
    from ..models.collection import Collection
    from ..models.link import Link


class Collections(pydantic.BaseModel):
    """
    Attributes:
        collections (list[Collection]): A list of Collection objects.
        links (list[Link]): A list of link objects to resources and related URLs.
    """

    collections: list[Collection] = pydantic.Field(
        ..., description="""A list of Collection objects.""", alias="collections"
    )
    links: list[Link] = pydantic.Field(
        ...,
        description="""A list of link objects to resources and related URLs.""",
        alias="links",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
