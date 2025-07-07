from typing import Literal, Union

from pydantic import BaseModel

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
        type (Union[Literal['Feature'], None]):  Default: 'Feature'.
        geometry (Union[None, PointGeometry, PolygonGeometry]): Defines the full footprint of the asset represented by
            the item.
    """

    id: str
    properties: "StacFeatureProperties"
    collection: str
    links: list["Link"]
    assets: "StacFeatureAssets"
    bbox: list[Union[float, int]]
    type: Union[Literal["Feature"], None] = "Feature"
    geometry: Union[None, PointGeometry, PolygonGeometry] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "id",
            "properties",
            "collection",
            "links",
            "assets",
            "bbox",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "id": str,
            "properties": object,
            "collection": str,
            "links": object,
            "assets": object,
            "bbox": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "type": object,
            "geometry": object,
        }
