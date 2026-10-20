# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

from ..models.acquisition_item_collection import AcquisitionItemCollection
from ..models.acquisition_item_type import AcquisitionItemType

if TYPE_CHECKING:
    from ..models.acquisition_item_properties import AcquisitionItemProperties
    from ..models.geo_json_geometry_collection import GeoJSONGeometryCollection
    from ..models.geo_json_line_string import GeoJSONLineString
    from ..models.geo_json_multi_line_string import GeoJSONMultiLineString
    from ..models.geo_json_multi_point import GeoJSONMultiPoint
    from ..models.geo_json_multi_polygon import GeoJSONMultiPolygon
    from ..models.geo_json_point import GeoJSONPoint
    from ..models.geo_json_polygon import GeoJSONPolygon
    from ..models.link import Link


class AcquisitionItem(pydantic.BaseModel):
    """
    Attributes:
        assets (dict):
        bbox (list[float]):
        collection ('AcquisitionItemCollection'):
        geometry (Union['GeoJSONGeometryCollection', 'GeoJSONLineString', 'GeoJSONMultiLineString', 'GeoJSONMultiPoint',
            'GeoJSONMultiPolygon', 'GeoJSONPoint', 'GeoJSONPolygon']): Search for items by performing intersection between
            their geometry and a provided GeoJSON geometry.
        id (str):
        links (list[Link]):
        stac_version (str):
        type_ ('AcquisitionItemType'):
        properties (Union[None, AcquisitionItemProperties]):
        stac_extensions (Union[None, list[str]]):
    """

    assets: dict = pydantic.Field(..., description=None, alias="assets")
    bbox: list[float] = pydantic.Field(..., description=None, alias="bbox")
    collection: AcquisitionItemCollection = pydantic.Field(
        ..., description=None, alias="collection"
    )
    geometry: Union[
        GeoJSONGeometryCollection,
        GeoJSONLineString,
        GeoJSONMultiLineString,
        GeoJSONMultiPoint,
        GeoJSONMultiPolygon,
        GeoJSONPoint,
        GeoJSONPolygon,
    ] = pydantic.Field(
        ...,
        description="""Search for items by performing intersection between their geometry and a provided GeoJSON geometry.""",
        alias="geometry",
    )
    id: str = pydantic.Field(..., description=None, alias="id")
    links: list[Link] = pydantic.Field(..., description=None, alias="links")
    stac_version: str = pydantic.Field(..., description=None, alias="stac_version")
    type_: AcquisitionItemType = pydantic.Field(..., description=None, alias="type")
    properties: Union[None, AcquisitionItemProperties] = pydantic.Field(
        default=None, description=None, alias="properties"
    )
    stac_extensions: Union[None, list[str]] = pydantic.Field(
        default=None, description=None, alias="stac_extensions"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
