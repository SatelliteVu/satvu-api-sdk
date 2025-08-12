from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.link import Link
from ..models.point_geometry import PointGeometry
from ..models.polygon_geometry import PolygonGeometry
from ..models.stac_feature_assets import StacFeatureAssets
from ..models.stac_feature_properties import StacFeatureProperties


class StacFeature(BaseModel):
    """
    Attributes:
        id (str): The unique identifier for this item within the collection.
        properties (StacFeatureProperties): A dictionary of additional metadata for the item.
        collection (str): The ID of the STAC Collection this item references to.
        links (list['Link']): A list of link objects to resources and related URLs.
        assets (StacFeatureAssets): A dictionary of asset objects that can be downloaded, each with a unique key.
        bbox (list[Union[float, int]]): The bounding box of the asset represented by this item.
        type_ (Union[Literal['Feature'], None]):  Default: 'Feature'.
        geometry (Union[None, PointGeometry, PolygonGeometry]): Defines the full footprint of the asset represented by
            the item.
    """

    id: str = Field(
        ...,
        description="The unique identifier for this item within the collection.",
        alias="id",
    )
    properties: "StacFeatureProperties" = Field(
        ...,
        description="A dictionary of additional metadata for the item.",
        alias="properties",
    )
    collection: str = Field(
        ...,
        description="The ID of the STAC Collection this item references to.",
        alias="collection",
    )
    links: list["Link"] = Field(
        ...,
        description="A list of link objects to resources and related URLs.",
        alias="links",
    )
    assets: "StacFeatureAssets" = Field(
        ...,
        description="A dictionary of asset objects that can be downloaded, each with a unique key.",
        alias="assets",
    )
    bbox: list[Union[float, int]] = Field(
        ...,
        description="The bounding box of the asset represented by this item.",
        alias="bbox",
    )
    type_: Union[Literal["Feature"], None] = Field(
        "Feature", description=None, alias="type"
    )
    geometry: Union[None, PointGeometry, PolygonGeometry] = Field(
        None,
        description="Defines the full footprint of the asset represented by the item.",
        alias="geometry",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
