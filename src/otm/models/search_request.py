from typing import Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from ..models.collections import Collections
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
        token (Union[None, str]): The pagination token.
        limit (Union[None, int]): The number of items to return per page. Default: 25.
        collections (Union[None, list[Collections]]): A list of collection types.
        ids (Union[None, list[UUID]]): A list of IDs.
        datetime_ (Union[None, str]):
        created_at (Union[None, str]): The datetime interval during which the entity was created.
        updated_at (Union[None, str]): The datetime interval during which the entity was last updated.
        properties (Union[FilterFields, None]): Allowed properties to filter a search. Filterable string fields allow
            one value or a list of values resulting in an equality or 'IN' comparison respectively. For numeric fields, one
            value similarly achieves an equality operation. A tuple of 2 values can also be provided to search inclusively
            between a range.
        intersects (Union[GeometryCollection, LineString, MultiLineString, MultiPoint, MultiPolygon, None, Point,
            Polygon]): A GeoJSON geometry to filter for. Items are returned if the geometry of the item intersects with the
            geometry provided.
        sort_by (Union[None, list['SortEntities']]): Sort the order in which results are returned.
    """

    token: Union[None, str] = Field(
        None, description="The pagination token.", alias="token"
    )
    limit: Union[None, int] = Field(
        25, description="The number of items to return per page.", alias="limit"
    )
    collections: Union[None, list[Collections]] = Field(
        None, description="A list of collection types.", alias="collections"
    )
    ids: Union[None, list[UUID]] = Field(
        None, description="A list of IDs.", alias="ids"
    )
    datetime_: Union[None, str] = Field(None, description=None, alias="datetime")
    created_at: Union[None, str] = Field(
        None,
        description="The datetime interval during which the entity was created.",
        alias="created_at",
    )
    updated_at: Union[None, str] = Field(
        None,
        description="The datetime interval during which the entity was last updated.",
        alias="updated_at",
    )
    properties: Union[FilterFields, None] = Field(
        None,
        description="Allowed properties to filter a search. Filterable string fields allow one value or a list of values resulting in an equality or 'IN' comparison respectively. For numeric fields, one value similarly achieves an equality operation. A tuple of 2 values can also be provided to search inclusively between a range.",
        alias="properties",
    )
    intersects: Union[
        GeometryCollection,
        LineString,
        MultiLineString,
        MultiPoint,
        MultiPolygon,
        None,
        Point,
        Polygon,
    ] = Field(
        None,
        description="A GeoJSON geometry to filter for. Items are returned if the geometry of the item intersects with the geometry provided.",
        alias="intersects",
    )
    sort_by: Union[None, list["SortEntities"]] = Field(
        None,
        description="Sort the order in which results are returned.",
        alias="sort_by",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
