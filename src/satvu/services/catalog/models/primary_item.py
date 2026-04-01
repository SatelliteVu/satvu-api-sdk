# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.primary_item_collection import PrimaryItemCollection
from ..models.primary_item_type import PrimaryItemType

if TYPE_CHECKING:
    from ..models.geo_json_geometry_collection import GeoJSONGeometryCollection
    from ..models.geo_json_line_string import GeoJSONLineString
    from ..models.geo_json_multi_line_string import GeoJSONMultiLineString
    from ..models.geo_json_multi_point import GeoJSONMultiPoint
    from ..models.geo_json_multi_polygon import GeoJSONMultiPolygon
    from ..models.geo_json_point import GeoJSONPoint
    from ..models.geo_json_polygon import GeoJSONPolygon
    from ..models.link import Link
    from ..models.primary_item_properties import PrimaryItemProperties


class PrimaryItem(BaseModel):
    """
    Attributes:
        assets (dict):
        bbox (list[float]):
        collection ('PrimaryItemCollection'):
        geometry (Union['GeoJSONGeometryCollection', 'GeoJSONLineString', 'GeoJSONMultiLineString', 'GeoJSONMultiPoint',
            'GeoJSONMultiPolygon', 'GeoJSONPoint', 'GeoJSONPolygon']): Search for items by performing intersection between
            their geometry and a provided GeoJSON geometry.
        id (str):
        links (list[Link]):
        stac_version (str):
        type_ ('PrimaryItemType'):
        properties (Union[None, PrimaryItemProperties]):
        stac_extensions (Union[None, list[str]]):
    """

    assets: dict = Field(..., description=None, alias="assets")
    bbox: list[float] = Field(..., description=None, alias="bbox")
    collection: PrimaryItemCollection = Field(..., description=None, alias="collection")
    geometry: Union[
        GeoJSONGeometryCollection,
        GeoJSONLineString,
        GeoJSONMultiLineString,
        GeoJSONMultiPoint,
        GeoJSONMultiPolygon,
        GeoJSONPoint,
        GeoJSONPolygon,
    ] = Field(
        ...,
        description="""Search for items by performing intersection between their geometry and a provided GeoJSON geometry.""",
        alias="geometry",
    )
    id: str = Field(..., description=None, alias="id")
    links: list[Link] = Field(..., description=None, alias="links")
    stac_version: str = Field(..., description=None, alias="stac_version")
    type_: PrimaryItemType = Field(..., description=None, alias="type")
    properties: Union[None, PrimaryItemProperties] = Field(
        default=None, description=None, alias="properties"
    )
    stac_extensions: Union[None, list[str]] = Field(
        default=None, description=None, alias="stac_extensions"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
