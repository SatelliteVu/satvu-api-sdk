"""Contains all the data models used in inputs/outputs"""

from .and_or_expression import AndOrExpression
from .and_or_expression_op import AndOrExpressionOp
from .arithmetic_expression import ArithmeticExpression
from .arithmetic_expression_op import ArithmeticExpressionOp
from .bbox_literal import BboxLiteral
from .binary_comparison_predicate import BinaryComparisonPredicate
from .binary_comparison_predicate_op import BinaryComparisonPredicateOp
from .client_credentials import ClientCredentials
from .client_id import ClientID
from .core_webhook import CoreWebhook
from .create_webhook_response import CreateWebhookResponse
from .credit_balance_response import CreditBalanceResponse
from .date_instant import DateInstant
from .edit_webhook_payload import EditWebhookPayload
from .error_response import ErrorResponse
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
from .list_response_context import ListResponseContext
from .list_webhook_response import ListWebhookResponse
from .not_expression import NotExpression
from .not_expression_op import NotExpressionOp
from .notification_category import NotificationCategory
from .notification_config import NotificationConfig
from .notification_description import NotificationDescription
from .notification_settings import NotificationSettings
from .notification_update import NotificationUpdate
from .post_webhook_response import PostWebhookResponse
from .property_ref import PropertyRef
from .reseller_notification_category import ResellerNotificationCategory
from .reseller_notification_config import ResellerNotificationConfig
from .reseller_notification_config_topic import ResellerNotificationConfigTopic
from .reseller_notification_description import ResellerNotificationDescription
from .reseller_notification_description_topic import (
    ResellerNotificationDescriptionTopic,
)
from .reseller_notification_update import ResellerNotificationUpdate
from .reseller_webhook_event import ResellerWebhookEvent
from .test_webhook_response import TestWebhookResponse
from .timestamp_instant import TimestampInstant
from .user_info import UserInfo
from .user_info_deprecated import UserInfoDeprecated
from .user_info_deprecated_user_metadata_type_0 import (
    UserInfoDeprecatedUserMetadataType0,
)
from .user_metadata import UserMetadata
from .user_settings import UserSettings
from .validation_error import ValidationError
from .verbose_notification import VerboseNotification
from .webhook_event import WebhookEvent
from .webhook_failure_title import WebhookFailureTitle
from .webhook_response import WebhookResponse
from .webhook_result import WebhookResult

__all__ = (
    "AndOrExpression",
    "AndOrExpressionOp",
    "ArithmeticExpression",
    "ArithmeticExpressionOp",
    "BboxLiteral",
    "BinaryComparisonPredicate",
    "BinaryComparisonPredicateOp",
    "ClientCredentials",
    "ClientID",
    "CoreWebhook",
    "CreateWebhookResponse",
    "CreditBalanceResponse",
    "DateInstant",
    "EditWebhookPayload",
    "ErrorResponse",
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
    "ListResponseContext",
    "ListWebhookResponse",
    "NotExpression",
    "NotExpressionOp",
    "NotificationCategory",
    "NotificationConfig",
    "NotificationDescription",
    "NotificationSettings",
    "NotificationUpdate",
    "PostWebhookResponse",
    "PropertyRef",
    "ResellerNotificationCategory",
    "ResellerNotificationConfig",
    "ResellerNotificationConfigTopic",
    "ResellerNotificationDescription",
    "ResellerNotificationDescriptionTopic",
    "ResellerNotificationUpdate",
    "ResellerWebhookEvent",
    "TestWebhookResponse",
    "TimestampInstant",
    "UserInfo",
    "UserInfoDeprecated",
    "UserInfoDeprecatedUserMetadataType0",
    "UserMetadata",
    "UserSettings",
    "ValidationError",
    "VerboseNotification",
    "WebhookEvent",
    "WebhookFailureTitle",
    "WebhookResponse",
    "WebhookResult",
)

# Ensure all Pydantic models have forward refs rebuilt
import inspect
import sys

from pydantic import BaseModel

_current_module = sys.modules[__name__]

for _obj in list(_current_module.__dict__.values()):
    if inspect.isclass(_obj) and issubclass(_obj, BaseModel) and _obj is not BaseModel:
        _obj.model_rebuild()
