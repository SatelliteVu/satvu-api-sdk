from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from typing import Union

    from ..models.link import Link


class TypesCatalog(BaseModel):
    """
    Attributes:
        description (str): The description of the Catalog. Example: This is a catalog.
        id (str): The identifier of the Catalog. Example: examples.
        links (list[Link]): A list of references to other documents.
        stac_version (str): The STAC version the Catalog implements. Example: 1.0.0.
        type_ (str): Catalog. Example: Catalog.
        conforms_to (Union[None, list[str]]):
        stac_extensions (Union[None, list[str]]): A list of extension identifiers the Catalog implements.
        title (Union[None, str]): The title of the Catalog. Example: Example Catalog.
    """

    description: str = Field(
        ..., description="The description of the Catalog.", alias="description"
    )
    id: str = Field(..., description="The identifier of the Catalog.", alias="id")
    links: list[Link] = Field(
        ..., description="A list of references to other documents.", alias="links"
    )
    stac_version: str = Field(
        ...,
        description="The STAC version the Catalog implements.",
        alias="stac_version",
    )
    type_: str = Field(..., description="Catalog.", alias="type")
    conforms_to: Union[None, list[str]] = Field(
        None, description=None, alias="conformsTo"
    )
    stac_extensions: Union[None, list[str]] = Field(
        None,
        description="A list of extension identifiers the Catalog implements.",
        alias="stac_extensions",
    )
    title: Union[None, str] = Field(
        None, description="The title of the Catalog.", alias="title"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
