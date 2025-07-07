from dataclasses import dataclass
from typing import TYPE_CHECKING, Union
from uuid import UUID

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


@dataclass
class SearchRequest:
    """
    Attributes:
        token (Union[None, str]): Pagination token.
        limit (Union[None, int]): Number of items to return per page. Default: 25.
        collections (Union[None, list[Collections]]): A list of collection types.
        ids (Union[None, list[UUID]]): A list of IDs.
        datetime_ (Union[None, str]):
        created_at (Union[None, str]): The datetime at which the entity was created.
        updated_at (Union[None, str]): The datetime at which the entity was last updated.
        properties (Union['FilterFields', None]): Allowed properties to filter a search. Filterable string fields allow
            one value or a list of values resulting in an equality or 'IN' comparison respectively. For numeric fields, one
            value similarly achieves an equality operation. A tuple of 2 values can also be provided to search inclusively
            between a range.
        intersects (Union['GeometryCollection', 'LineString', 'MultiLineString', 'MultiPoint', 'MultiPolygon', 'Point',
            'Polygon', None]): A GeoJSON geometry to filter for. Items are returned if the geometry of theitem intersects
            with the geometry provided.
        sort_by (Union[None, list['SortEntities']]): Sort the order in which results are returned.
    """

    token: Union[None, str] = None
    limit: Union[None, int] = 25
    collections: Union[None, list[Collections]] = None
    ids: Union[None, list[UUID]] = None
    datetime_: Union[None, str] = None
    created_at: Union[None, str] = None
    updated_at: Union[None, str] = None
    properties: Union["FilterFields", None] = None
    intersects: Union[
        "GeometryCollection",
        "LineString",
        "MultiLineString",
        "MultiPoint",
        "MultiPolygon",
        "Point",
        "Polygon",
        None,
    ] = None
    sort_by: Union[None, list["SortEntities"]] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {}

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {}

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "token": object,
            "limit": object,
            "collections": object,
            "ids": object,
            "datetime": object,
            "created_at": object,
            "updated_at": object,
            "properties": object,
            "intersects": object,
            "sort_by": object,
        }
