# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

if TYPE_CHECKING:
    from ..models.asset_bands import AssetBands


class Asset(pydantic.BaseModel):
    """
    Attributes:
        href (str): URI to the asset object. Can be relative or absolute.
        description (Union[None, str]): A description of the asset.
        raster_bands (Union[None, AssetBands]): Bands
        roles (Union[None, list[str]]): The semantic roles of the asset.
        title (Union[None, str]): The title of the asset.
        type_ (Union[None, str]): Media type of the asset.
    """

    href: str = pydantic.Field(
        ...,
        description="""URI to the asset object. Can be relative or absolute.""",
        alias="href",
    )
    description: Union[None, str] = pydantic.Field(
        default=None, description="""A description of the asset.""", alias="description"
    )
    raster_bands: Union[None, AssetBands] = pydantic.Field(
        default=None, description="""Bands""", alias="raster:bands"
    )
    roles: Union[None, list[str]] = pydantic.Field(
        default=None, description="""The semantic roles of the asset.""", alias="roles"
    )
    title: Union[None, str] = pydantic.Field(
        default=None, description="""The title of the asset.""", alias="title"
    )
    type_: Union[None, str] = pydantic.Field(
        default=None, description="""Media type of the asset.""", alias="type"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
