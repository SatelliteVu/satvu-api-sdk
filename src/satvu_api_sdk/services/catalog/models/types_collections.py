from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.collection import Collection
    from ..models.link import Link


class TypesCollections(BaseModel):
    """
    Attributes:
        collections (list[Collection]):
        links (list[Link]):
    """

    collections: list[Collection] = Field(..., description=None, alias="collections")
    links: list[Link] = Field(..., description=None, alias="links")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
