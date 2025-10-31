from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.stac_metadata_1_assets import StacMetadata1Assets
    from ..models.stac_properties_v41 import StacPropertiesV41
    from ..models.stac_properties_v71 import StacPropertiesV71
    from ..models.stac_properties_v81 import StacPropertiesV81


class StacMetadata1(BaseModel):
    """
    Attributes:
        id (str): The unique image identifier.
        collection (str): Collection ID.
        assets (StacMetadata1Assets): A dictionary of asset objects that can be downloaded, each with a unique key.
        bbox (list[float | int]): The bounding box of the asset represented by this item.
        properties (Union['StacPropertiesV41', 'StacPropertiesV71', 'StacPropertiesV81']): A dictionary of additional
            metadata for the item.
    """

    id: str = Field(..., description="The unique image identifier.", alias="id")
    collection: str = Field(..., description="Collection ID.", alias="collection")
    assets: "StacMetadata1Assets" = Field(
        ...,
        description="A dictionary of asset objects that can be downloaded, each with a unique key.",
        alias="assets",
    )
    bbox: list[float | int] = Field(
        ...,
        description="The bounding box of the asset represented by this item.",
        alias="bbox",
    )
    properties: Union["StacPropertiesV41", "StacPropertiesV71", "StacPropertiesV81"] = (
        Field(
            ...,
            description="A dictionary of additional metadata for the item.",
            alias="properties",
        )
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
