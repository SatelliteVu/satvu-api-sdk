# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from ..models.collections import Collections

if TYPE_CHECKING:
    from ..models.filter_fields import FilterFields
    from ..models.geometry_collection import GeometryCollection
    from ..models.line_string import LineString
    from ..models.multi_line_string import MultiLineString
    from ..models.multi_point import MultiPoint
    from ..models.multi_polygon import MultiPolygon
    from ..models.point import Point
    from ..models.polygon import Polygon
    from ..models.sort_entities import SortEntities


class SearchRequest(BaseModel):
    """
    Attributes:
        token (None | str): The pagination token.
        limit (int | None): The number of items to return per page. Default: 25.
        collections (list['Collections'] | None): A list of collection types.
        ids (list[UUID] | None): A list of IDs.
        series_ids (list[UUID] | None): Filter results by series IDs. Only orders belonging to these series are
            returned.
        datetime_ (None | str):
        created_at (None | str): The datetime interval during which the entity was created.
        updated_at (None | str): The datetime interval during which the entity was last updated.
        properties (Union['FilterFields', None]): Allowed properties to filter a search. Filterable string fields allow
            one value or a list of values resulting in an equality or 'IN' comparison respectively. For numeric fields, one
            value similarly achieves an equality operation. A tuple of 2 values can also be provided to search inclusively
            between a range.
        intersects (Union['GeometryCollection', 'LineString', 'MultiLineString', 'MultiPoint', 'MultiPolygon', 'Point',
            'Polygon', None]): A GeoJSON geometry to filter for. Items are returned if the geometry of the item intersects
            with the geometry provided.
        sort_by (list[SortEntities] | None): Sort the order in which results are returned.
    """

    token: None | str = Field(
        default=None, description="""The pagination token.""", alias="token"
    )
    limit: int | None = Field(
        default=25,
        description="""The number of items to return per page.""",
        alias="limit",
    )
    collections: list[Collections] | None = Field(
        default=None, description="""A list of collection types.""", alias="collections"
    )
    ids: list[UUID] | None = Field(
        default=None, description="""A list of IDs.""", alias="ids"
    )
    series_ids: list[UUID] | None = Field(
        default=None,
        description="""Filter results by series IDs. Only orders belonging to these series are returned.""",
        alias="series_ids",
    )
    datetime_: None | str = Field(default=None, description=None, alias="datetime")
    created_at: None | str = Field(
        default=None,
        description="""The datetime interval during which the entity was created.""",
        alias="created_at",
    )
    updated_at: None | str = Field(
        default=None,
        description="""The datetime interval during which the entity was last updated.""",
        alias="updated_at",
    )
    properties: Union[FilterFields, None] = Field(
        default=None,
        description="""Allowed properties to filter a search. Filterable string fields allow one value or a list of values resulting in an equality or 'IN' comparison respectively. For numeric fields, one value similarly achieves an equality operation. A tuple of 2 values can also be provided to search inclusively between a range.""",
        alias="properties",
    )
    intersects: Union[
        GeometryCollection,
        LineString,
        MultiLineString,
        MultiPoint,
        MultiPolygon,
        Point,
        Polygon,
        None,
    ] = Field(
        default=None,
        description="""A GeoJSON geometry to filter for. Items are returned if the geometry of the item intersects with the geometry provided.""",
        alias="intersects",
    )
    sort_by: list[SortEntities] | None = Field(
        default=None,
        description="""Sort the order in which results are returned.""",
        alias="sort_by",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
