from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from typing import Union

    from ..models.asset_raster_bands import AssetRasterBands


class Asset(BaseModel):
    """
    Attributes:
        href (str): URI to the asset object. Can be relative or absolute.
        description (Union[None, str]): A description of the asset.
        raster_bands (Union[None, AssetRasterBands]):
        roles (Union[None, list[str]]): The semantic roles of the asset.
        title (Union[None, str]): The title of of the asset.
        type_ (Union[None, str]): Media type of the asset.
    """

    href: str = Field(
        ...,
        description="URI to the asset object. Can be relative or absolute.",
        alias="href",
    )
    description: Union[None, str] = Field(
        None, description="A description of the asset.", alias="description"
    )
    raster_bands: Union[None, "AssetRasterBands"] = Field(
        None, description=None, alias="raster:bands"
    )
    roles: Union[None, list[str]] = Field(
        None, description="The semantic roles of the asset.", alias="roles"
    )
    title: Union[None, str] = Field(
        None, description="The title of of the asset.", alias="title"
    )
    type_: Union[None, str] = Field(
        None, description="Media type of the asset.", alias="type"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
