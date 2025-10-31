from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.collection import Collection
    from ..models.link import Link


class Collections(BaseModel):
    """
    Attributes:
        collections (list[Collection]): A list of Collection objects.
        links (list[Link]): A list of link objects to resources and related URLs.
    """

    collections: list[Collection] = Field(
        ..., description="A list of Collection objects.", alias="collections"
    )
    links: list[Link] = Field(
        ...,
        description="A list of link objects to resources and related URLs.",
        alias="links",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
