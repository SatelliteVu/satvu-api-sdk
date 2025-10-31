from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.stac_metadata_assets import StacMetadataAssets
    from ..models.stac_properties_v4 import StacPropertiesV4
    from ..models.stac_properties_v7 import StacPropertiesV7
    from ..models.stac_properties_v8 import StacPropertiesV8


class StacMetadata(BaseModel):
    """
    Attributes:
        id (str): The unique image identifier.
        collection (str): Collection ID.
        assets (StacMetadataAssets): A dictionary of asset objects that can be downloaded, each with a unique key.
        bbox (list[float | int]): The bounding box of the asset represented by this item.
        properties (Union['StacPropertiesV4', 'StacPropertiesV7', 'StacPropertiesV8']): A dictionary of additional
            metadata for the item.
    """

    id: str = Field(..., description="The unique image identifier.", alias="id")
    collection: str = Field(..., description="Collection ID.", alias="collection")
    assets: "StacMetadataAssets" = Field(
        ...,
        description="A dictionary of asset objects that can be downloaded, each with a unique key.",
        alias="assets",
    )
    bbox: list[float | int] = Field(
        ...,
        description="The bounding box of the asset represented by this item.",
        alias="bbox",
    )
    properties: Union["StacPropertiesV4", "StacPropertiesV7", "StacPropertiesV8"] = (
        Field(
            ...,
            description="A dictionary of additional metadata for the item.",
            alias="properties",
        )
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
