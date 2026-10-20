# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

if TYPE_CHECKING:
    from ..models.feature_properties import FeatureProperties
    from ..models.geo_json_geometry_collection import GeoJSONGeometryCollection
    from ..models.geo_json_line_string import GeoJSONLineString
    from ..models.geo_json_multi_line_string import GeoJSONMultiLineString
    from ..models.geo_json_multi_point import GeoJSONMultiPoint
    from ..models.geo_json_multi_polygon import GeoJSONMultiPolygon
    from ..models.geo_json_point import GeoJSONPoint
    from ..models.geo_json_polygon import GeoJSONPolygon
    from ..models.link import Link


class Feature(pydantic.BaseModel):
    """
    Attributes:
        bbox (list[float]): Bounding Box of the asset represented by the Item.
        collection (str): The ID of the Collection the Item references to. Example: collection.
        geometry (Union['GeoJSONGeometryCollection', 'GeoJSONLineString', 'GeoJSONMultiLineString', 'GeoJSONMultiPoint',
            'GeoJSONMultiPolygon', 'GeoJSONPoint', 'GeoJSONPolygon']): Search for items by performing intersection between
            their geometry and a provided GeoJSON geometry.
        id (str): The identifier of the Item, unique within the Collection that contains the Item. Example: item.
        links (list[Link]): A list of link objects to resources and related URLs.
        properties (FeatureProperties): Properties of the Item
        stac_version (str): The STAC version the Item implements. Example: 1.0.0.
        type_ (str): Feature. Example: Feature.
        assets (Union[None, dict]): Mapping of asset objects that can be downloaded, each with a unique key.
        stac_extensions (Union[None, list[str]]): A list of extensions the Item implements.
    """

    bbox: list[float] = pydantic.Field(
        ...,
        description="""Bounding Box of the asset represented by the Item.""",
        alias="bbox",
    )
    collection: str = pydantic.Field(
        ...,
        description="""The ID of the Collection the Item references to.""",
        alias="collection",
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
    id: str = pydantic.Field(
        ...,
        description="""The identifier of the Item, unique within the Collection that contains the Item.""",
        alias="id",
    )
    links: list[Link] = pydantic.Field(
        ...,
        description="""A list of link objects to resources and related URLs.""",
        alias="links",
    )
    properties: FeatureProperties = pydantic.Field(
        ..., description="""Properties of the Item""", alias="properties"
    )
    stac_version: str = pydantic.Field(
        ...,
        description="""The STAC version the Item implements.""",
        alias="stac_version",
    )
    type_: str = pydantic.Field(..., description="""Feature.""", alias="type")
    assets: Union[None, dict] = pydantic.Field(
        default=None,
        description="""Mapping of asset objects that can be downloaded, each with a unique key.""",
        alias="assets",
    )
    stac_extensions: Union[None, list[str]] = pydantic.Field(
        default=None,
        description="""A list of extensions the Item implements.""",
        alias="stac_extensions",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
