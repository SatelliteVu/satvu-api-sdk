# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/models_init.py.jinja
"""Contains all the data models used in inputs/outputs"""

from .acquisition_feature_collection import AcquisitionFeatureCollection
from .acquisition_feature_collection_type import AcquisitionFeatureCollectionType
from .acquisition_item import AcquisitionItem
from .acquisition_item_collection import AcquisitionItemCollection
from .acquisition_item_type import AcquisitionItemType
from .acquisition_queryables import AcquisitionQueryables
from .and_or_expression import AndOrExpression
from .and_or_expression_op import AndOrExpressionOp
from .api_error import ApiError
from .arithmetic_expression import ArithmeticExpression
from .arithmetic_expression_op import ArithmeticExpressionOp
from .asset import Asset
from .bbox_literal import BboxLiteral
from .binary_comparison_predicate import BinaryComparisonPredicate
from .binary_comparison_predicate_op import BinaryComparisonPredicateOp
from .catalog import Catalog
from .collection import Collection
from .collections import Collections
from .conformance import Conformance
from .date_instant import DateInstant
from .error import Error
from .extent import Extent
from .feature import Feature
from .feature_collection import FeatureCollection
from .generic_item import GenericItem
from .generic_item_properties import GenericItemProperties
from .generic_item_type import GenericItemType
from .geo_json_geometry_collection import GeoJSONGeometryCollection
from .geo_json_geometry_collection_type import GeoJSONGeometryCollectionType
from .geo_json_line_string import GeoJSONLineString
from .geo_json_line_string_type import GeoJSONLineStringType
from .geo_json_multi_line_string import GeoJSONMultiLineString
from .geo_json_multi_line_string_type import GeoJSONMultiLineStringType
from .geo_json_multi_point import GeoJSONMultiPoint
from .geo_json_multi_point_type import GeoJSONMultiPointType
from .geo_json_multi_polygon import GeoJSONMultiPolygon
from .geo_json_multi_polygon_type import GeoJSONMultiPolygonType
from .geo_json_point import GeoJSONPoint
from .geo_json_point_type import GeoJSONPointType
from .geo_json_polygon import GeoJSONPolygon
from .geo_json_polygon_type import GeoJSONPolygonType
from .geojson_crs import GeojsonCRS
from .geojson_geometry import GeojsonGeometry
from .get_search_intersects import GetSearchIntersects
from .http_error import HttpError
from .is_between_predicate import IsBetweenPredicate
from .is_between_predicate_op import IsBetweenPredicateOp
from .is_in_list_predicate import IsInListPredicate
from .is_in_list_predicate_op import IsInListPredicateOp
from .is_like_predicate import IsLikePredicate
from .is_like_predicate_op import IsLikePredicateOp
from .is_null_predicate import IsNullPredicate
from .is_null_predicate_op import IsNullPredicateOp
from .link import Link
from .not_expression import NotExpression
from .not_expression_op import NotExpressionOp
from .post_collection_search_input import PostCollectionSearchInput
from .post_search_input import PostSearchInput
from .primary_feature_collection import PrimaryFeatureCollection
from .primary_feature_collection_type import PrimaryFeatureCollectionType
from .primary_item import PrimaryItem
from .primary_item_collection import PrimaryItemCollection
from .primary_item_properties import PrimaryItemProperties
from .primary_item_type import PrimaryItemType
from .primary_queryables import PrimaryQueryables
from .property_ref import PropertyRef
from .queryable_property import QueryableProperty
from .queryables import Queryables
from .search_response import SearchResponse
from .sort_by_element import SortByElement
from .spatial_extent import SpatialExtent
from .stac_geometry import StacGeometry
from .surface_brightness_temperature_feature_collection import (
    SurfaceBrightnessTemperatureFeatureCollection,
)
from .surface_brightness_temperature_feature_collection_type import (
    SurfaceBrightnessTemperatureFeatureCollectionType,
)
from .surface_brightness_temperature_item import SurfaceBrightnessTemperatureItem
from .surface_brightness_temperature_item_collection import (
    SurfaceBrightnessTemperatureItemCollection,
)
from .surface_brightness_temperature_item_properties import (
    SurfaceBrightnessTemperatureItemProperties,
)
from .surface_brightness_temperature_item_type import (
    SurfaceBrightnessTemperatureItemType,
)
from .surface_brightness_temperature_queryables import (
    SurfaceBrightnessTemperatureQueryables,
)
from .temporal_extent import TemporalExtent
from .timestamp_instant import TimestampInstant
from .visual_feature_collection import VisualFeatureCollection
from .visual_feature_collection_type import VisualFeatureCollectionType
from .visual_item import VisualItem
from .visual_item_collection import VisualItemCollection
from .visual_item_properties import VisualItemProperties
from .visual_item_type import VisualItemType
from .visual_queryables import VisualQueryables

__all__ = (
    "AcquisitionFeatureCollection",
    "AcquisitionFeatureCollectionType",
    "AcquisitionItem",
    "AcquisitionItemCollection",
    "AcquisitionItemType",
    "AcquisitionQueryables",
    "AndOrExpression",
    "AndOrExpressionOp",
    "ApiError",
    "ArithmeticExpression",
    "ArithmeticExpressionOp",
    "Asset",
    "BboxLiteral",
    "BinaryComparisonPredicate",
    "BinaryComparisonPredicateOp",
    "Catalog",
    "Collection",
    "Collections",
    "Conformance",
    "DateInstant",
    "Error",
    "Extent",
    "Feature",
    "FeatureCollection",
    "GenericItem",
    "GenericItemProperties",
    "GenericItemType",
    "GeojsonCRS",
    "GeojsonGeometry",
    "GeoJSONGeometryCollection",
    "GeoJSONGeometryCollectionType",
    "GeoJSONLineString",
    "GeoJSONLineStringType",
    "GeoJSONMultiLineString",
    "GeoJSONMultiLineStringType",
    "GeoJSONMultiPoint",
    "GeoJSONMultiPointType",
    "GeoJSONMultiPolygon",
    "GeoJSONMultiPolygonType",
    "GeoJSONPoint",
    "GeoJSONPointType",
    "GeoJSONPolygon",
    "GeoJSONPolygonType",
    "GetSearchIntersects",
    "HttpError",
    "IsBetweenPredicate",
    "IsBetweenPredicateOp",
    "IsInListPredicate",
    "IsInListPredicateOp",
    "IsLikePredicate",
    "IsLikePredicateOp",
    "IsNullPredicate",
    "IsNullPredicateOp",
    "Link",
    "NotExpression",
    "NotExpressionOp",
    "PostCollectionSearchInput",
    "PostSearchInput",
    "PrimaryFeatureCollection",
    "PrimaryFeatureCollectionType",
    "PrimaryItem",
    "PrimaryItemCollection",
    "PrimaryItemProperties",
    "PrimaryItemType",
    "PrimaryQueryables",
    "PropertyRef",
    "QueryableProperty",
    "Queryables",
    "SearchResponse",
    "SortByElement",
    "SpatialExtent",
    "StacGeometry",
    "SurfaceBrightnessTemperatureFeatureCollection",
    "SurfaceBrightnessTemperatureFeatureCollectionType",
    "SurfaceBrightnessTemperatureItem",
    "SurfaceBrightnessTemperatureItemCollection",
    "SurfaceBrightnessTemperatureItemProperties",
    "SurfaceBrightnessTemperatureItemType",
    "SurfaceBrightnessTemperatureQueryables",
    "TemporalExtent",
    "TimestampInstant",
    "VisualFeatureCollection",
    "VisualFeatureCollectionType",
    "VisualItem",
    "VisualItemCollection",
    "VisualItemProperties",
    "VisualItemType",
    "VisualQueryables",
)

# Ensure all Pydantic models have forward refs rebuilt
import inspect
import sys

from pydantic import BaseModel

_current_module = sys.modules[__name__]

for _obj in list(_current_module.__dict__.values()):
    if inspect.isclass(_obj) and issubclass(_obj, BaseModel) and _obj is not BaseModel:
        _obj.model_rebuild()
