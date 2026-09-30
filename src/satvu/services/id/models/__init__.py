# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/models_init.py.jinja
"""Contains all the data models used in inputs/outputs"""

from .client_credentials import ClientCredentials
from .client_id import ClientID
from .company_kyc_status_update_payload import CompanyKYCStatusUpdatePayload
from .company_kyc_status_update_webhook import CompanyKYCStatusUpdateWebhook
from .core_webhook import CoreWebhook
from .create_webhook_response import CreateWebhookResponse
from .edit_webhook_payload import EditWebhookPayload
from .end_user_kyc_status_update_payload import EndUserKYCStatusUpdatePayload
from .end_user_kyc_status_update_webhook import EndUserKYCStatusUpdateWebhook
from .error_response import ErrorResponse
from .http_validation_error import HTTPValidationError
from .kyc_status import KycStatus
from .link import Link
from .list_response_context import ListResponseContext
from .list_webhook_response import ListWebhookResponse
from .notification_category import NotificationCategory
from .notification_config import NotificationConfig
from .notification_description import NotificationDescription
from .notification_settings import NotificationSettings
from .notification_update import NotificationUpdate
from .post_webhook_response import PostWebhookResponse
from .product import Product
from .reseller_webhook_event import ResellerWebhookEvent
from .tasking_order_expired_payload_v2 import TaskingOrderExpiredPayloadV2
from .tasking_order_expired_webhook_v2 import TaskingOrderExpiredWebhookV2
from .tasking_order_fulfilled_payload_v2 import TaskingOrderFulfilledPayloadV2
from .tasking_order_fulfilled_payload_v3 import TaskingOrderFulfilledPayloadV3
from .tasking_order_fulfilled_webhook_v2 import TaskingOrderFulfilledWebhookV2
from .tasking_order_fulfilled_webhook_v3 import TaskingOrderFulfilledWebhookV3
from .test_webhook_response import TestWebhookResponse
from .user_info import UserInfo
from .user_metadata import UserMetadata
from .user_settings import UserSettings
from .validation_error import ValidationError
from .verbose_notification import VerboseNotification
from .webhook_event import WebhookEvent
from .webhook_failure_title import WebhookFailureTitle
from .webhook_response import WebhookResponse
from .webhook_result import WebhookResult

__all__ = (
    "ClientCredentials",
    "ClientID",
    "CompanyKYCStatusUpdatePayload",
    "CompanyKYCStatusUpdateWebhook",
    "CoreWebhook",
    "CreateWebhookResponse",
    "EditWebhookPayload",
    "EndUserKYCStatusUpdatePayload",
    "EndUserKYCStatusUpdateWebhook",
    "ErrorResponse",
    "HTTPValidationError",
    "KycStatus",
    "Link",
    "ListResponseContext",
    "ListWebhookResponse",
    "NotificationCategory",
    "NotificationConfig",
    "NotificationDescription",
    "NotificationSettings",
    "NotificationUpdate",
    "PostWebhookResponse",
    "Product",
    "ResellerWebhookEvent",
    "TaskingOrderExpiredPayloadV2",
    "TaskingOrderExpiredWebhookV2",
    "TaskingOrderFulfilledPayloadV2",
    "TaskingOrderFulfilledPayloadV3",
    "TaskingOrderFulfilledWebhookV2",
    "TaskingOrderFulfilledWebhookV3",
    "TestWebhookResponse",
    "UserInfo",
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
