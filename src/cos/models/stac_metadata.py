from typing import Union

from pydantic import BaseModel, Field

from ..models.stac_metadata_assets import StacMetadataAssets
from ..models.stac_properties_v4 import StacPropertiesV4
from ..models.stac_properties_v6 import StacPropertiesV6
from ..models.stac_properties_v7 import StacPropertiesV7


class StacMetadata(BaseModel):
    """
    Attributes:
        id (str): The unique image identifier.
        collection (str): Collection ID.
        assets (StacMetadataAssets): A dictionary of asset objects that can be downloaded, each with a unique key.
        bbox (list[Union[float, int]]): The bounding box of the asset represented by this item.
        properties (Union[StacPropertiesV4, StacPropertiesV6, StacPropertiesV7]): A dictionary of additional metadata
            for the item.
    """

    id: str = Field(..., description="The unique image identifier.")
    collection: str = Field(..., description="Collection ID.")
    assets: "StacMetadataAssets" = Field(
        ...,
        description="A dictionary of asset objects that can be downloaded, each with a unique key.",
    )
    bbox: list[Union[float, int]] = Field(
        ..., description="The bounding box of the asset represented by this item."
    )
    properties: Union[StacPropertiesV4, StacPropertiesV6, StacPropertiesV7] = Field(
        ..., description="A dictionary of additional metadata for the item."
    )
