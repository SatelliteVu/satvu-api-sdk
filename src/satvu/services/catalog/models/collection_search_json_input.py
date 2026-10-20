# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

if TYPE_CHECKING:
    from ..models.geo_json_geometry_collection import GeoJSONGeometryCollection
    from ..models.geo_json_line_string import GeoJSONLineString
    from ..models.geo_json_multi_line_string import GeoJSONMultiLineString
    from ..models.geo_json_multi_point import GeoJSONMultiPoint
    from ..models.geo_json_multi_polygon import GeoJSONMultiPolygon
    from ..models.geo_json_point import GeoJSONPoint
    from ..models.geo_json_polygon import GeoJSONPolygon
    from ..models.sort_by_element import SortByElement


class CollectionSearchJsonInput(pydantic.BaseModel):
    """
    Attributes:
        bbox (Union[None, list[float]]): Array of floats representing a bounding box.
        datetime_ (None | str): Single date+time, or a range with '/' separator. Example: 1985-04-12T23:20:50.52Z/...
        filter_ (Union[None, dict]): Filters using Common Query Language (CQL2).
        ids (Union[None, list[str]]): Array of Item IDs to return.
        intersects (Union[None, Union['GeoJSONGeometryCollection', 'GeoJSONLineString', 'GeoJSONMultiLineString',
            'GeoJSONMultiPoint', 'GeoJSONMultiPolygon', 'GeoJSONPoint', 'GeoJSONPolygon']]): Search for items by performing
            intersection between their geometry and a provided GeoJSON geometry.
        limit (int | None): The maximum number of results to return per page. Example: 10.
        sortby (Union[None, list[SortByElement]]): An array of objects containing a property name and sort direction.
        token (Union[None, str]): The pagination token.
    """

    bbox: Union[None, list[float]] = pydantic.Field(
        default=None,
        description="""Array of floats representing a bounding box.""",
        alias="bbox",
    )
    datetime_: None | str = pydantic.Field(
        default=None,
        description="""Single date+time, or a range with '/' separator.""",
        alias="datetime",
    )
    filter_: Union[None, dict] = pydantic.Field(
        default=None,
        description="""Filters using Common Query Language (CQL2).""",
        alias="filter",
    )
    ids: Union[None, list[str]] = pydantic.Field(
        default=None, description="""Array of Item IDs to return.""", alias="ids"
    )
    intersects: Union[
        None,
        Union[
            GeoJSONGeometryCollection,
            GeoJSONLineString,
            GeoJSONMultiLineString,
            GeoJSONMultiPoint,
            GeoJSONMultiPolygon,
            GeoJSONPoint,
            GeoJSONPolygon,
        ],
    ] = pydantic.Field(
        default=None,
        description="""Search for items by performing intersection between their geometry and a provided GeoJSON geometry.""",
        alias="intersects",
    )
    limit: int | None = pydantic.Field(
        default=None,
        description="""The maximum number of results to return per page.""",
        alias="limit",
    )
    sortby: Union[None, list[SortByElement]] = pydantic.Field(
        default=None,
        description="""An array of objects containing a property name and sort direction.""",
        alias="sortby",
    )
    token: Union[None, str] = pydantic.Field(
        default=None, description="""The pagination token.""", alias="token"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
