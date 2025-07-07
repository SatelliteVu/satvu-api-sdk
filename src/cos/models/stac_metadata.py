from typing import Union

from pydantic import BaseModel

from ..models.stac_metadata_assets import StacMetadataAssets
from ..models.stac_properties_v4 import StacPropertiesV4
from ..models.stac_properties_v5 import StacPropertiesV5


class StacMetadata(BaseModel):
    """
    Attributes:
        id (str): The unique image identifier.
        collection (str): Collection ID.
        assets (StacMetadataAssets): A dictionary of asset objects that can be downloaded, each with a unique key.
        bbox (list[Union[float, int]]): The bounding box of the asset represented by this item.
        properties (Union[StacPropertiesV4, StacPropertiesV5]): A dictionary of additional metadata for the item.
    """

    id: str
    collection: str
    assets: "StacMetadataAssets"
    bbox: list[Union[float, int]]
    properties: Union[StacPropertiesV4, StacPropertiesV5]
