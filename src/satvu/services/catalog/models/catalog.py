# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

if TYPE_CHECKING:
    from ..models.link import Link


class Catalog(pydantic.BaseModel):
    """
    Attributes:
        description (str): The description of the Catalog. Example: This is a catalog.
        id (str): The identifier of the Catalog. Example: examples.
        links (list[Link]): A list of references to other documents.
        stac_version (str): The STAC version the Catalog implements. Example: 1.0.0.
        type_ (str): Catalog. Example: Catalog.
        conforms_to (Union[None, list[str]]): A list of all conformance classes implemented.
        stac_extensions (Union[None, list[str]]): A list of extension identifiers the Catalog implements.
        title (Union[None, str]): The title of the Catalog. Example: Example Catalog.
    """

    description: str = pydantic.Field(
        ..., description="""The description of the Catalog.""", alias="description"
    )
    id: str = pydantic.Field(
        ..., description="""The identifier of the Catalog.""", alias="id"
    )
    links: list[Link] = pydantic.Field(
        ..., description="""A list of references to other documents.""", alias="links"
    )
    stac_version: str = pydantic.Field(
        ...,
        description="""The STAC version the Catalog implements.""",
        alias="stac_version",
    )
    type_: str = pydantic.Field(..., description="""Catalog.""", alias="type")
    conforms_to: Union[None, list[str]] = pydantic.Field(
        default=None,
        description="""A list of all conformance classes implemented.""",
        alias="conformsTo",
    )
    stac_extensions: Union[None, list[str]] = pydantic.Field(
        default=None,
        description="""A list of extension identifiers the Catalog implements.""",
        alias="stac_extensions",
    )
    title: Union[None, str] = pydantic.Field(
        default=None, description="""The title of the Catalog.""", alias="title"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
