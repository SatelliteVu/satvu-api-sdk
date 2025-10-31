"""Contains all the data models used in inputs/outputs"""

from .client_credentials import ClientCredentials
from .client_id import ClientID
from .core_webhook import CoreWebhook
from .create_webhook_response import CreateWebhookResponse
from .credit_balance_response import CreditBalanceResponse
from .edit_webhook_payload import EditWebhookPayload
from .error_response import ErrorResponse
from .http_validation_error import HTTPValidationError
from .link import Link
from .list_response_context import ListResponseContext
from .list_webhook_response import ListWebhookResponse
from .notification_category import NotificationCategory
from .notification_config import NotificationConfig
from .notification_description import NotificationDescription
from .notification_settings import NotificationSettings
from .notification_update import NotificationUpdate
from .post_webhook_response import PostWebhookResponse
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
from .user_info import UserInfo
from .user_info_deprecated import UserInfoDeprecated
from .user_info_deprecated_user_metadata_type_0 import (
    UserInfoDeprecatedUserMetadataType0,
)
from .user_metadata import UserMetadata
from .user_metadata_1 import UserMetadata1
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
    "CoreWebhook",
    "CreateWebhookResponse",
    "CreditBalanceResponse",
    "EditWebhookPayload",
    "ErrorResponse",
    "HTTPValidationError",
    "Link",
    "ListResponseContext",
    "ListWebhookResponse",
    "NotificationCategory",
    "NotificationConfig",
    "NotificationDescription",
    "NotificationSettings",
    "NotificationUpdate",
    "PostWebhookResponse",
    "ResellerNotificationCategory",
    "ResellerNotificationConfig",
    "ResellerNotificationConfigTopic",
    "ResellerNotificationDescription",
    "ResellerNotificationDescriptionTopic",
    "ResellerNotificationUpdate",
    "ResellerWebhookEvent",
    "TestWebhookResponse",
    "UserInfo",
    "UserInfoDeprecated",
    "UserInfoDeprecatedUserMetadataType0",
    "UserMetadata",
    "UserMetadata1",
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
