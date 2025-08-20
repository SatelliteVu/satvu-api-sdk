from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.feature_assets import FeatureAssets
from ..models.feature_properties import FeatureProperties
from ..models.geojson_geometry import GeojsonGeometry
from ..models.link import Link


class Feature(BaseModel):
    """
    Attributes:
        bbox (list[float]): Bounding Box of the asset represented by the Item.
        collection (str): The ID of the Collection the Item references to. Example: collection.
        geometry (GeojsonGeometry): Defines the full footprint of the asset represented by the Item, formatted according
            to RFC 7946 section 3.1.
        id (str): The identifier of the Item, unique within the Collection that contains the Item. Example: item.
        links (list[Link]): A list of link objects to resources and related URLs.
        properties (FeatureProperties):
        stac_version (str): The STAC version the Item implements. Example: 1.0.0.
        type_ (str): Feature. Example: Feature.
        assets (Union[None, FeatureAssets]): Dictionary of asset objects that can be downloaded, each with a unique key.
        stac_extensions (Union[None, list[str]]): A list of extensions the Item implements.
    """

    bbox: list[float] = Field(
        ...,
        description="Bounding Box of the asset represented by the Item.",
        alias="bbox",
    )
    collection: str = Field(
        ...,
        description="The ID of the Collection the Item references to.",
        alias="collection",
    )
    geometry: "GeojsonGeometry" = Field(
        ...,
        description="Defines the full footprint of the asset represented by the Item, formatted according to RFC 7946 section 3.1.",
        alias="geometry",
    )
    id: str = Field(
        ...,
        description="The identifier of the Item, unique within the Collection that contains the Item.",
        alias="id",
    )
    links: list[Link] = Field(
        ...,
        description="A list of link objects to resources and related URLs.",
        alias="links",
    )
    properties: "FeatureProperties" = Field(..., description=None, alias="properties")
    stac_version: str = Field(
        ..., description="The STAC version the Item implements.", alias="stac_version"
    )
    type_: str = Field(..., description="Feature.", alias="type")
    assets: Union[None, "FeatureAssets"] = Field(
        None,
        description="Dictionary of asset objects that can be downloaded, each with a unique key.",
        alias="assets",
    )
    stac_extensions: Union[None, list[str]] = Field(
        None,
        description="A list of extensions the Item implements.",
        alias="stac_extensions",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
