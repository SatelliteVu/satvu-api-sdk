from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from typing import Union

    from ..models.and_or_expression import AndOrExpression
    from ..models.binary_comparison_predicate import BinaryComparisonPredicate
    from ..models.geo_json_geometry_collection_1 import GeoJSONGeometryCollection1
    from ..models.geo_json_line_string import GeoJSONLineString
    from ..models.geo_json_multi_line_string import GeoJSONMultiLineString
    from ..models.geo_json_multi_point import GeoJSONMultiPoint
    from ..models.geo_json_multi_polygon import GeoJSONMultiPolygon
    from ..models.geo_json_point import GeoJSONPoint
    from ..models.geo_json_polygon import GeoJSONPolygon
    from ..models.is_between_predicate import IsBetweenPredicate
    from ..models.is_in_list_predicate import IsInListPredicate
    from ..models.is_like_predicate import IsLikePredicate
    from ..models.is_null_predicate import IsNullPredicate
    from ..models.not_expression import NotExpression
    from ..models.types_sort_by_element import TypesSortByElement


class PostSearchInput(BaseModel):
    """
    Attributes:
        bbox (Union[None, list[float]]): Array of floats representing a bounding box. Only features that have a geometry
            that intersects the bounding box are selected. Example: [-90, -45, 90, 45].
        collections (Union[None, list[str]]): Array of Collection IDs to include in the search for items. Only Item
            objects in one of the provided collections will be searched. Example: ['collection1', 'collection2'].
        datetime_ (Union[None, str]): Single date+time, or a range ('/') separator, formatted to RFC3339 section 5.6.
            Use double dots for open ranges. Example: 1985-04-12T23:20:50.52Z/...
        filter_ (Union['AndOrExpression', 'BinaryComparisonPredicate', 'IsBetweenPredicate', 'IsInListPredicate',
            'IsLikePredicate', 'IsNullPredicate', 'NotExpression', bool]): Filter using Common Query Language (CQL2).
        ids (Union[None, list[str]]): Array of Item IDs to return. Example: ['item1', 'item2'].
        intersects (Union['GeoJSONGeometryCollection1', 'GeoJSONLineString', 'GeoJSONMultiLineString',
            'GeoJSONMultiPoint', 'GeoJSONMultiPolygon', 'GeoJSONPoint', 'GeoJSONPolygon']): Search for items by performing
            intersection between their geometry and a provided GeoJSON geometry.
        limit (Union[None, int]): The maximum number of results to return per page. Example: 10.
        sortby (Union[None, list[TypesSortByElement]]): An array of objects containing a property name and sort
            direction.
        token (Union[None, str]): The pagination token.
    """

    bbox: Union[None, list[float]] = Field(
        None,
        description="Array of floats representing a bounding box. Only features that have a geometry that intersects the bounding box are selected.",
        alias="bbox",
    )
    collections: Union[None, list[str]] = Field(
        None,
        description="Array of Collection IDs to include in the search for items. Only Item objects in one of the provided collections will be searched.",
        alias="collections",
    )
    datetime_: Union[None, str] = Field(
        None,
        description="Single date+time, or a range ('/') separator, formatted to RFC3339 section 5.6. Use double dots for open ranges.",
        alias="datetime",
    )
    filter_: Union[
        "AndOrExpression",
        "BinaryComparisonPredicate",
        "IsBetweenPredicate",
        "IsInListPredicate",
        "IsLikePredicate",
        "IsNullPredicate",
        "NotExpression",
        bool,
    ] = Field(
        None, description="Filter using Common Query Language (CQL2).", alias="filter"
    )
    ids: Union[None, list[str]] = Field(
        None, description="Array of Item IDs to return.", alias="ids"
    )
    intersects: Union[
        "GeoJSONGeometryCollection1",
        "GeoJSONLineString",
        "GeoJSONMultiLineString",
        "GeoJSONMultiPoint",
        "GeoJSONMultiPolygon",
        "GeoJSONPoint",
        "GeoJSONPolygon",
    ] = Field(
        None,
        description="Search for items by performing intersection between their geometry and a provided GeoJSON geometry.",
        alias="intersects",
    )
    limit: Union[None, int] = Field(
        None,
        description="The maximum number of results to return per page.",
        alias="limit",
    )
    sortby: Union[None, list[TypesSortByElement]] = Field(
        None,
        description="An array of objects containing a property name and sort direction.",
        alias="sortby",
    )
    token: Union[None, str] = Field(
        None, description="The pagination token.", alias="token"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
