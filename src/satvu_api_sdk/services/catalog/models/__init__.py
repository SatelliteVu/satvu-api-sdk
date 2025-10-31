"""Contains all the data models used in inputs/outputs"""

from .and_or_expression import AndOrExpression
from .and_or_expression_op import AndOrExpressionOp
from .api_error import ApiError
from .arithmetic_expression import ArithmeticExpression
from .arithmetic_expression_op import ArithmeticExpressionOp
from .asset import Asset
from .asset_bands import AssetBands
from .asset_bands_data_type_of_the_band import AssetBandsDataTypeOfTheBand
from .asset_bands_nodata_type_1 import AssetBandsNodataType1
from .asset_bands_pixel_sampling_in_the_band import AssetBandsPixelSamplingInTheBand
from .asset_bands_statistics import AssetBandsStatistics
from .bbox_literal import BboxLiteral
from .binary_comparison_predicate import BinaryComparisonPredicate
from .binary_comparison_predicate_op import BinaryComparisonPredicateOp
from .catalog import Catalog
from .collection import Collection
from .collections import Collections
from .conformance import Conformance
from .cql_2_queryables_schema import Cql2QueryablesSchema
from .cql_2_queryables_schema_properties import Cql2QueryablesSchemaProperties
from .date_instant import DateInstant
from .error import Error
from .extent import Extent
from .feature import Feature
from .feature_assets import FeatureAssets
from .feature_collection import FeatureCollection
from .feature_properties import FeatureProperties
from .filter_ import Filter
from .geo_json_geometry_collection import GeoJSONGeometryCollection
from .geo_json_geometry_collection_1 import GeoJSONGeometryCollection1
from .geo_json_geometry_collection_1_type import GeoJSONGeometryCollection1Type
from .geo_json_geometry_collection_type import GeoJSONGeometryCollectionType
from .geo_json_line_string import GeoJSONLineString
from .geo_json_line_string_1 import GeoJSONLineString1
from .geo_json_line_string_1_type import GeoJSONLineString1Type
from .geo_json_line_string_type import GeoJSONLineStringType
from .geo_json_multi_line_string import GeoJSONMultiLineString
from .geo_json_multi_line_string_1 import GeoJSONMultiLineString1
from .geo_json_multi_line_string_1_type import GeoJSONMultiLineString1Type
from .geo_json_multi_line_string_type import GeoJSONMultiLineStringType
from .geo_json_multi_point import GeoJSONMultiPoint
from .geo_json_multi_point_1 import GeoJSONMultiPoint1
from .geo_json_multi_point_1_type import GeoJSONMultiPoint1Type
from .geo_json_multi_point_type import GeoJSONMultiPointType
from .geo_json_multi_polygon import GeoJSONMultiPolygon
from .geo_json_multi_polygon_1 import GeoJSONMultiPolygon1
from .geo_json_multi_polygon_1_type import GeoJSONMultiPolygon1Type
from .geo_json_multi_polygon_type import GeoJSONMultiPolygonType
from .geo_json_point import GeoJSONPoint
from .geo_json_point_1 import GeoJSONPoint1
from .geo_json_point_1_type import GeoJSONPoint1Type
from .geo_json_point_type import GeoJSONPointType
from .geo_json_polygon import GeoJSONPolygon
from .geo_json_polygon_1 import GeoJSONPolygon1
from .geo_json_polygon_1_type import GeoJSONPolygon1Type
from .geo_json_polygon_type import GeoJSONPolygonType
from .geojson_crs import GeojsonCRS
from .geojson_crs_properties import GeojsonCRSProperties
from .geojson_geometry import GeojsonGeometry
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
from .link_body import LinkBody
from .not_expression import NotExpression
from .not_expression_op import NotExpressionOp
from .post_search_input import PostSearchInput
from .property_ref import PropertyRef
from .queryable_property import QueryableProperty
from .search_response import SearchResponse
from .sort_by_element import SortByElement
from .spatial_extent import SpatialExtent
from .stac_geometry import StacGeometry
from .temporal_extent import TemporalExtent
from .timestamp_instant import TimestampInstant

__all__ = (
    "AndOrExpression",
    "AndOrExpressionOp",
    "ApiError",
    "ArithmeticExpression",
    "ArithmeticExpressionOp",
    "Asset",
    "AssetBands",
    "AssetBandsDataTypeOfTheBand",
    "AssetBandsNodataType1",
    "AssetBandsPixelSamplingInTheBand",
    "AssetBandsStatistics",
    "BboxLiteral",
    "BinaryComparisonPredicate",
    "BinaryComparisonPredicateOp",
    "Catalog",
    "Collection",
    "Collections",
    "Conformance",
    "Cql2QueryablesSchema",
    "Cql2QueryablesSchemaProperties",
    "DateInstant",
    "Error",
    "Extent",
    "Feature",
    "FeatureAssets",
    "FeatureCollection",
    "FeatureProperties",
    "Filter",
    "GeojsonCRS",
    "GeojsonCRSProperties",
    "GeojsonGeometry",
    "GeoJSONGeometryCollection",
    "GeoJSONGeometryCollection1",
    "GeoJSONGeometryCollection1Type",
    "GeoJSONGeometryCollectionType",
    "GeoJSONLineString",
    "GeoJSONLineString1",
    "GeoJSONLineString1Type",
    "GeoJSONLineStringType",
    "GeoJSONMultiLineString",
    "GeoJSONMultiLineString1",
    "GeoJSONMultiLineString1Type",
    "GeoJSONMultiLineStringType",
    "GeoJSONMultiPoint",
    "GeoJSONMultiPoint1",
    "GeoJSONMultiPoint1Type",
    "GeoJSONMultiPointType",
    "GeoJSONMultiPolygon",
    "GeoJSONMultiPolygon1",
    "GeoJSONMultiPolygon1Type",
    "GeoJSONMultiPolygonType",
    "GeoJSONPoint",
    "GeoJSONPoint1",
    "GeoJSONPoint1Type",
    "GeoJSONPointType",
    "GeoJSONPolygon",
    "GeoJSONPolygon1",
    "GeoJSONPolygon1Type",
    "GeoJSONPolygonType",
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
    "LinkBody",
    "NotExpression",
    "NotExpressionOp",
    "PostSearchInput",
    "PropertyRef",
    "QueryableProperty",
    "SearchResponse",
    "SortByElement",
    "SpatialExtent",
    "StacGeometry",
    "TemporalExtent",
    "TimestampInstant",
)

# Ensure all Pydantic models have forward refs rebuilt
import inspect
import sys

from pydantic import BaseModel

_current_module = sys.modules[__name__]

for _obj in list(_current_module.__dict__.values()):
    if inspect.isclass(_obj) and issubclass(_obj, BaseModel) and _obj is not BaseModel:
        _obj.model_rebuild()
