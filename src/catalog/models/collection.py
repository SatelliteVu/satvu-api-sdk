from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.extent import Extent
    from ..models.link import Link


class Collection(BaseModel):
    """
    Attributes:
        description (str): The description of the Collection. Example: This is a Collection.
        extent (Extent): Spatial and temporal extents.
        id (str): The identifier of the Collection, unique across the Catalog. Example: collection.
        license_ (str): The Collection's license.
        links (list[Link]): A list of references to other documents.
        stac_version (str): The STAC version the Collection implements. Example: 1.0.0.
        type_ (str): Collection. Example: Collection.
        keywords (Union[None, list[str]]): A list of keywords describing the Collection.
        stac_extensions (Union[None, list[str]]): A list of extension identifiers the Collection implements.
        title (Union[None, str]): The title of the Collection. Example: Example Collection.
    """

    description: str = Field(
        ..., description="The description of the Collection.", alias="description"
    )
    extent: "Extent" = Field(
        ..., description="Spatial and temporal extents.", alias="extent"
    )
    id: str = Field(
        ...,
        description="The identifier of the Collection, unique across the Catalog.",
        alias="id",
    )
    license_: str = Field(..., description="The Collection's license.", alias="license")
    links: list[Link] = Field(
        ..., description="A list of references to other documents.", alias="links"
    )
    stac_version: str = Field(
        ...,
        description="The STAC version the Collection implements.",
        alias="stac_version",
    )
    type_: str = Field(..., description="Collection.", alias="type")
    keywords: Union[None, list[str]] = Field(
        None,
        description="A list of keywords describing the Collection.",
        alias="keywords",
    )
    stac_extensions: Union[None, list[str]] = Field(
        None,
        description="A list of extension identifiers the Collection implements.",
        alias="stac_extensions",
    )
    title: Union[None, str] = Field(
        None, description="The title of the Collection.", alias="title"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
