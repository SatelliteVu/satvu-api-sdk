"""Contains all the data models used in inputs/outputs"""

from .and_or_expression import AndOrExpression
from .and_or_expression_op import AndOrExpressionOp
from .arithmetic_expression import ArithmeticExpression
from .arithmetic_expression_op import ArithmeticExpressionOp
from .bbox_literal import BboxLiteral
from .binary_comparison_predicate import BinaryComparisonPredicate
from .binary_comparison_predicate_op import BinaryComparisonPredicateOp
from .date_instant import DateInstant
from .download_order_collections_type_0_item import DownloadOrderCollectionsType0Item
from .feature_collection_order import FeatureCollectionOrder
from .feature_order import FeatureOrder
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
from .geojson_polygon import GeojsonPolygon
from .http_exception_response import HttpExceptionResponse
from .http_validation_error import HTTPValidationError
from .is_between_predicate import IsBetweenPredicate
from .is_between_predicate_op import IsBetweenPredicateOp
from .is_in_list_predicate import IsInListPredicate
from .is_in_list_predicate_op import IsInListPredicateOp
from .is_like_predicate import IsLikePredicate
from .is_like_predicate_op import IsLikePredicateOp
from .is_null_predicate import IsNullPredicate
from .is_null_predicate_op import IsNullPredicateOp
from .link import Link
from .link_body_type_0 import LinkBodyType0
from .link_method import LinkMethod
from .not_expression import NotExpression
from .not_expression_op import NotExpressionOp
from .order import Order
from .order_download_url import OrderDownloadUrl
from .order_edit_payload import OrderEditPayload
from .order_item_download_url import OrderItemDownloadUrl
from .order_page import OrderPage
from .order_submission_payload import OrderSubmissionPayload
from .point_geometry import PointGeometry
from .polygon import Polygon
from .polygon_1 import Polygon1
from .polygon_geometry import PolygonGeometry
from .price import Price
from .property_ref import PropertyRef
from .reseller_feature_collection_order import ResellerFeatureCollectionOrder
from .reseller_submission_order_payload import ResellerSubmissionOrderPayload
from .satvu_filter import SatvuFilter
from .stac_metadata import StacMetadata
from .stac_metadata_assets import StacMetadataAssets
from .stac_properties_v4 import StacPropertiesV4
from .stac_properties_v6 import StacPropertiesV6
from .stac_properties_v6_processing_software_name_version import (
    StacPropertiesV6ProcessingSoftwareNameVersion,
)
from .stac_properties_v7 import StacPropertiesV7
from .stac_properties_v7_processing_software_name_version import (
    StacPropertiesV7ProcessingSoftwareNameVersion,
)
from .timestamp_instant import TimestampInstant
from .validation_error import ValidationError

__all__ = (
    "AndOrExpression",
    "AndOrExpressionOp",
    "ArithmeticExpression",
    "ArithmeticExpressionOp",
    "BboxLiteral",
    "BinaryComparisonPredicate",
    "BinaryComparisonPredicateOp",
    "DateInstant",
    "DownloadOrderCollectionsType0Item",
    "FeatureCollectionOrder",
    "FeatureOrder",
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
    "GeojsonPolygon",
    "GeoJSONPolygon",
    "GeoJSONPolygon1",
    "GeoJSONPolygon1Type",
    "GeoJSONPolygonType",
    "HttpExceptionResponse",
    "HTTPValidationError",
    "IsBetweenPredicate",
    "IsBetweenPredicateOp",
    "IsInListPredicate",
    "IsInListPredicateOp",
    "IsLikePredicate",
    "IsLikePredicateOp",
    "IsNullPredicate",
    "IsNullPredicateOp",
    "Link",
    "LinkBodyType0",
    "LinkMethod",
    "NotExpression",
    "NotExpressionOp",
    "Order",
    "OrderDownloadUrl",
    "OrderEditPayload",
    "OrderItemDownloadUrl",
    "OrderPage",
    "OrderSubmissionPayload",
    "PointGeometry",
    "Polygon",
    "Polygon1",
    "PolygonGeometry",
    "Price",
    "PropertyRef",
    "ResellerFeatureCollectionOrder",
    "ResellerSubmissionOrderPayload",
    "SatvuFilter",
    "StacMetadata",
    "StacMetadataAssets",
    "StacPropertiesV4",
    "StacPropertiesV6",
    "StacPropertiesV6ProcessingSoftwareNameVersion",
    "StacPropertiesV7",
    "StacPropertiesV7ProcessingSoftwareNameVersion",
    "TimestampInstant",
    "ValidationError",
)

# Ensure all Pydantic models have forward refs rebuilt
import inspect
import sys

from pydantic import BaseModel

_current_module = sys.modules[__name__]

for _obj in list(_current_module.__dict__.values()):
    if inspect.isclass(_obj) and issubclass(_obj, BaseModel) and _obj is not BaseModel:
        _obj.model_rebuild()
