# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/models_init.py.jinja
"""Contains all the data models used in inputs/outputs"""

from .download_order_collections_item import DownloadOrderCollectionsItem
from .download_order_item_primary_formats_item import (
    DownloadOrderItemPrimaryFormatsItem,
)
from .download_order_primary_formats_item import DownloadOrderPrimaryFormatsItem
from .download_pending import DownloadPending
from .download_progress import DownloadProgress
from .eo_band import EoBand
from .feature_collection_order import FeatureCollectionOrder
from .feature_order import FeatureOrder
from .geojson_polygon import GeojsonPolygon
from .http_exception_response import HttpExceptionResponse
from .http_validation_error import HTTPValidationError
from .legacy_link import LegacyLink
from .link import Link
from .method import Method
from .order import Order
from .order_download_url import OrderDownloadUrl
from .order_edit_payload import OrderEditPayload
from .order_item_download_url import OrderItemDownloadUrl
from .order_item_price import OrderItemPrice
from .order_page import OrderPage
from .order_price import OrderPrice
from .order_pricing import OrderPricing
from .order_submission_payload import OrderSubmissionPayload
from .point_geometry import PointGeometry
from .polygon import Polygon
from .polygon_geometry import PolygonGeometry
from .price_information import PriceInformation
from .price_request import PriceRequest
from .reseller_feature_collection_order import ResellerFeatureCollectionOrder
from .reseller_order_price import ResellerOrderPrice
from .reseller_price_request import ResellerPriceRequest
from .reseller_submission_order_payload import ResellerSubmissionOrderPayload
from .response_context import ResponseContext
from .satvu_cloud_confidence import SatvuCloudConfidence
from .satvu_filter import SatvuFilter
from .search_request import SearchRequest
from .stac_link import StacLink
from .stac_metadata import StacMetadata
from .stac_properties_acquisition import StacPropertiesAcquisition
from .stac_properties_v4 import StacPropertiesV4
from .stac_properties_v7 import StacPropertiesV7
from .validation_error import ValidationError

__all__ = (
    "DownloadOrderCollectionsItem",
    "DownloadOrderItemPrimaryFormatsItem",
    "DownloadOrderPrimaryFormatsItem",
    "DownloadPending",
    "DownloadProgress",
    "EoBand",
    "FeatureCollectionOrder",
    "FeatureOrder",
    "GeojsonPolygon",
    "HttpExceptionResponse",
    "HTTPValidationError",
    "LegacyLink",
    "Link",
    "Method",
    "Order",
    "OrderDownloadUrl",
    "OrderEditPayload",
    "OrderItemDownloadUrl",
    "OrderItemPrice",
    "OrderPage",
    "OrderPrice",
    "OrderPricing",
    "OrderSubmissionPayload",
    "PointGeometry",
    "Polygon",
    "PolygonGeometry",
    "PriceInformation",
    "PriceRequest",
    "ResellerFeatureCollectionOrder",
    "ResellerOrderPrice",
    "ResellerPriceRequest",
    "ResellerSubmissionOrderPayload",
    "ResponseContext",
    "SatvuCloudConfidence",
    "SatvuFilter",
    "SearchRequest",
    "StacLink",
    "StacMetadata",
    "StacPropertiesAcquisition",
    "StacPropertiesV4",
    "StacPropertiesV7",
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
