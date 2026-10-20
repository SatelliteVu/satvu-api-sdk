# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/models_init.py.jinja
"""Contains all the data models used in inputs/outputs"""

from .acquisition_feature_collection import AcquisitionFeatureCollection
from .acquisition_feature_collection_type import AcquisitionFeatureCollectionType
from .acquisition_item import AcquisitionItem
from .acquisition_item_collection import AcquisitionItemCollection
from .acquisition_item_properties import AcquisitionItemProperties
from .acquisition_item_type import AcquisitionItemType
from .acquisition_queryables import AcquisitionQueryables
from .and_or_expression import AndOrExpression
from .and_or_expression_op import AndOrExpressionOp
from .api_error import ApiError
from .arithmetic_expression import ArithmeticExpression
from .arithmetic_expression_op import ArithmeticExpressionOp
from .asset import Asset
from .asset_bands import AssetBands
from .asset_bands_nodata_type_1 import AssetBandsNodataType1
from .asset_bands_statistics import AssetBandsStatistics
from .bbox_literal import BboxLiteral
from .binary_comparison_predicate import BinaryComparisonPredicate
from .binary_comparison_predicate_op import BinaryComparisonPredicateOp
from .catalog import Catalog
from .collection import Collection
from .collection_search_json_input import CollectionSearchJsonInput
from .collection_search_json_response_429 import CollectionSearchJsonResponse429
from .collection_search_text_response_429 import CollectionSearchTextResponse429
from .collections import Collections
from .conformance import Conformance
from .data_type_of_the_band import DataTypeOfTheBand
from .date_instant import DateInstant
from .error import Error
from .extent import Extent
from .feature import Feature
from .feature_collection import FeatureCollection
from .feature_properties import FeatureProperties
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
from .get_acquisition_item_response_429 import GetAcquisitionItemResponse429
from .get_collection_response_429 import GetCollectionResponse429
from .get_item_response_429 import GetItemResponse429
from .get_primary_item_response_429 import GetPrimaryItemResponse429
from .get_surface_brightness_temperature_item_response_429 import (
    GetSurfaceBrightnessTemperatureItemResponse429,
)
from .http_error import HttpError
from .is_between_predicate import IsBetweenPredicate
from .is_between_predicate_op import IsBetweenPredicateOp
from .is_in_list_predicate import IsInListPredicate
from .is_in_list_predicate_op import IsInListPredicateOp
from .is_like_predicate import IsLikePredicate
from .is_like_predicate_op import IsLikePredicateOp
from .is_null_predicate import IsNullPredicate
from .is_null_predicate_op import IsNullPredicateOp
from .landing_page_response_429 import LandingPageResponse429
from .link import Link
from .list_acquisition_items_response_429 import ListAcquisitionItemsResponse429
from .list_acquisition_queryables_response_429 import (
    ListAcquisitionQueryablesResponse429,
)
from .list_collection_items_response_429 import ListCollectionItemsResponse429
from .list_collection_queryables_response_429 import ListCollectionQueryablesResponse429
from .list_collections_response_429 import ListCollectionsResponse429
from .list_conformance_classes_response_429 import ListConformanceClassesResponse429
from .list_primary_items_response_429 import ListPrimaryItemsResponse429
from .list_primary_queryables_response_429 import ListPrimaryQueryablesResponse429
from .list_queryables_response_429 import ListQueryablesResponse429
from .list_surface_brightness_temperature_items_response_429 import (
    ListSurfaceBrightnessTemperatureItemsResponse429,
)
from .list_surface_brightness_temperature_queryables_response_429 import (
    ListSurfaceBrightnessTemperatureQueryablesResponse429,
)
from .not_expression import NotExpression
from .not_expression_op import NotExpressionOp
from .pixel_sampling_in_the_band import PixelSamplingInTheBand
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
from .search_json_input import SearchJsonInput
from .search_json_response_429 import SearchJsonResponse429
from .search_response import SearchResponse
from .search_text_response_429 import SearchTextResponse429
from .sort_by_element import SortByElement
from .spatial_extent import SpatialExtent
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

__all__ = (
    "AcquisitionFeatureCollection",
    "AcquisitionFeatureCollectionType",
    "AcquisitionItem",
    "AcquisitionItemCollection",
    "AcquisitionItemProperties",
    "AcquisitionItemType",
    "AcquisitionQueryables",
    "AndOrExpression",
    "AndOrExpressionOp",
    "ApiError",
    "ArithmeticExpression",
    "ArithmeticExpressionOp",
    "Asset",
    "AssetBands",
    "AssetBandsNodataType1",
    "AssetBandsStatistics",
    "BboxLiteral",
    "BinaryComparisonPredicate",
    "BinaryComparisonPredicateOp",
    "Catalog",
    "Collection",
    "Collections",
    "CollectionSearchJsonInput",
    "CollectionSearchJsonResponse429",
    "CollectionSearchTextResponse429",
    "Conformance",
    "DataTypeOfTheBand",
    "DateInstant",
    "Error",
    "Extent",
    "Feature",
    "FeatureCollection",
    "FeatureProperties",
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
    "GetAcquisitionItemResponse429",
    "GetCollectionResponse429",
    "GetItemResponse429",
    "GetPrimaryItemResponse429",
    "GetSurfaceBrightnessTemperatureItemResponse429",
    "HttpError",
    "IsBetweenPredicate",
    "IsBetweenPredicateOp",
    "IsInListPredicate",
    "IsInListPredicateOp",
    "IsLikePredicate",
    "IsLikePredicateOp",
    "IsNullPredicate",
    "IsNullPredicateOp",
    "LandingPageResponse429",
    "Link",
    "ListAcquisitionItemsResponse429",
    "ListAcquisitionQueryablesResponse429",
    "ListCollectionItemsResponse429",
    "ListCollectionQueryablesResponse429",
    "ListCollectionsResponse429",
    "ListConformanceClassesResponse429",
    "ListPrimaryItemsResponse429",
    "ListPrimaryQueryablesResponse429",
    "ListQueryablesResponse429",
    "ListSurfaceBrightnessTemperatureItemsResponse429",
    "ListSurfaceBrightnessTemperatureQueryablesResponse429",
    "NotExpression",
    "NotExpressionOp",
    "PixelSamplingInTheBand",
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
    "SearchJsonInput",
    "SearchJsonResponse429",
    "SearchResponse",
    "SearchTextResponse429",
    "SortByElement",
    "SpatialExtent",
    "SurfaceBrightnessTemperatureFeatureCollection",
    "SurfaceBrightnessTemperatureFeatureCollectionType",
    "SurfaceBrightnessTemperatureItem",
    "SurfaceBrightnessTemperatureItemCollection",
    "SurfaceBrightnessTemperatureItemProperties",
    "SurfaceBrightnessTemperatureItemType",
    "SurfaceBrightnessTemperatureQueryables",
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
