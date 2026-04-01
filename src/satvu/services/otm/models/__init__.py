# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/models_init.py.jinja
"""Contains all the data models used in inputs/outputs"""

from .asset import Asset
from .assured_feasibility_fields import AssuredFeasibilityFields
from .assured_feasibility_fields_with_addons import AssuredFeasibilityFieldsWithAddons
from .assured_feasibility_response_feature import AssuredFeasibilityResponseFeature
from .assured_feasibility_response_properties import (
    AssuredFeasibilityResponseProperties,
)
from .assured_order_request import AssuredOrderRequest
from .assured_order_request_properties import AssuredOrderRequestProperties
from .assured_stored_feasibility_request_properties import (
    AssuredStoredFeasibilityRequestProperties,
)
from .collection import Collection
from .collections import Collections
from .day_night_mode import DayNightMode
from .direction import Direction
from .edit_order_payload import EditOrderPayload
from .edit_order_properties import EditOrderProperties
from .error_response import ErrorResponse
from .extra_ignore_assured_feasibility_response_properties import (
    ExtraIgnoreAssuredFeasibilityResponseProperties,
)
from .feasibility_request import FeasibilityRequest
from .feasibility_request_status import FeasibilityRequestStatus
from .feasibility_response import FeasibilityResponse
from .filter_ import Filter
from .filter_fields import FilterFields
from .full_well_capacitance import FullWellCapacitance
from .geometry_collection import GeometryCollection
from .get_assured_order_properties import GetAssuredOrderProperties
from .get_order_response import GetOrderResponse
from .get_standard_order_properties import GetStandardOrderProperties
from .http_validation_error import HTTPValidationError
from .line_string import LineString
from .link import Link
from .link_1 import Link1
from .list_stored_orders_response import ListStoredOrdersResponse
from .modify_feasibility_request import ModifyFeasibilityRequest
from .modify_feasibility_request_properties import ModifyFeasibilityRequestProperties
from .multi_line_string import MultiLineString
from .multi_point import MultiPoint
from .multi_polygon import MultiPolygon
from .order_item_download_url import OrderItemDownloadUrl
from .order_modification_price import OrderModificationPrice
from .order_price import OrderPrice
from .order_status import OrderStatus
from .outage import Outage
from .point import Point
from .point_geometry import PointGeometry
from .polygon import Polygon
from .polygon_geometry import PolygonGeometry
from .price import Price
from .price_information import PriceInformation
from .price_request import PriceRequest
from .primary_format import PrimaryFormat
from .readout_mode import ReadoutMode
from .request_method import RequestMethod
from .reseller_assured_order_request import ResellerAssuredOrderRequest
from .reseller_get_order_response import ResellerGetOrderResponse
from .reseller_search_response_feature_assured_order_request import (
    ResellerSearchResponseFeatureAssuredOrderRequest,
)
from .reseller_search_response_feature_standard_order_request import (
    ResellerSearchResponseFeatureStandardOrderRequest,
)
from .reseller_standard_order_request import ResellerStandardOrderRequest
from .reseller_stored_order_response import ResellerStoredOrderResponse
from .response_context import ResponseContext
from .search_assured_order_properties import SearchAssuredOrderProperties
from .search_request import SearchRequest
from .search_response import SearchResponse
from .search_response_feature_assured_feasibility_request import (
    SearchResponseFeatureAssuredFeasibilityRequest,
)
from .search_response_feature_assured_feasibility_response import (
    SearchResponseFeatureAssuredFeasibilityResponse,
)
from .search_response_feature_assured_order_request import (
    SearchResponseFeatureAssuredOrderRequest,
)
from .search_response_feature_standard_feasibility_request import (
    SearchResponseFeatureStandardFeasibilityRequest,
)
from .search_response_feature_standard_feasibility_response import (
    SearchResponseFeatureStandardFeasibilityResponse,
)
from .search_response_feature_standard_order_request import (
    SearchResponseFeatureStandardOrderRequest,
)
from .search_standard_order_properties import SearchStandardOrderProperties
from .sort_entities import SortEntities
from .sortable_field import SortableField
from .stac_feature import StacFeature
from .standard_feasibility_response_feature import StandardFeasibilityResponseFeature
from .standard_feasibility_response_properties import (
    StandardFeasibilityResponseProperties,
)
from .standard_order_fields_with_addons import StandardOrderFieldsWithAddons
from .standard_order_request import StandardOrderRequest
from .standard_order_request_properties import StandardOrderRequestProperties
from .standard_price_request_properties import StandardPriceRequestProperties
from .standard_request_properties import StandardRequestProperties
from .standard_stored_feasibility_request_properties import (
    StandardStoredFeasibilityRequestProperties,
)
from .stored_assured_order_request_properties import StoredAssuredOrderRequestProperties
from .stored_feasibility_feature_collection import StoredFeasibilityFeatureCollection
from .stored_feasibility_request import StoredFeasibilityRequest
from .stored_order_response import StoredOrderResponse
from .stored_standard_order_request_properties import (
    StoredStandardOrderRequestProperties,
)
from .validation_error import ValidationError
from .validation_error_detail import ValidationErrorDetail
from .validation_error_response import ValidationErrorResponse

__all__ = (
    "Asset",
    "AssuredFeasibilityFields",
    "AssuredFeasibilityFieldsWithAddons",
    "AssuredFeasibilityResponseFeature",
    "AssuredFeasibilityResponseProperties",
    "AssuredOrderRequest",
    "AssuredOrderRequestProperties",
    "AssuredStoredFeasibilityRequestProperties",
    "Collection",
    "Collections",
    "DayNightMode",
    "Direction",
    "EditOrderPayload",
    "EditOrderProperties",
    "ErrorResponse",
    "ExtraIgnoreAssuredFeasibilityResponseProperties",
    "FeasibilityRequest",
    "FeasibilityRequestStatus",
    "FeasibilityResponse",
    "Filter",
    "FilterFields",
    "FullWellCapacitance",
    "GeometryCollection",
    "GetAssuredOrderProperties",
    "GetOrderResponse",
    "GetStandardOrderProperties",
    "HTTPValidationError",
    "LineString",
    "Link",
    "Link1",
    "ListStoredOrdersResponse",
    "ModifyFeasibilityRequest",
    "ModifyFeasibilityRequestProperties",
    "MultiLineString",
    "MultiPoint",
    "MultiPolygon",
    "OrderItemDownloadUrl",
    "OrderModificationPrice",
    "OrderPrice",
    "OrderStatus",
    "Outage",
    "Point",
    "PointGeometry",
    "Polygon",
    "PolygonGeometry",
    "Price",
    "PriceInformation",
    "PriceRequest",
    "PrimaryFormat",
    "ReadoutMode",
    "RequestMethod",
    "ResellerAssuredOrderRequest",
    "ResellerGetOrderResponse",
    "ResellerSearchResponseFeatureAssuredOrderRequest",
    "ResellerSearchResponseFeatureStandardOrderRequest",
    "ResellerStandardOrderRequest",
    "ResellerStoredOrderResponse",
    "ResponseContext",
    "SearchAssuredOrderProperties",
    "SearchRequest",
    "SearchResponse",
    "SearchResponseFeatureAssuredFeasibilityRequest",
    "SearchResponseFeatureAssuredFeasibilityResponse",
    "SearchResponseFeatureAssuredOrderRequest",
    "SearchResponseFeatureStandardFeasibilityRequest",
    "SearchResponseFeatureStandardFeasibilityResponse",
    "SearchResponseFeatureStandardOrderRequest",
    "SearchStandardOrderProperties",
    "SortableField",
    "SortEntities",
    "StacFeature",
    "StandardFeasibilityResponseFeature",
    "StandardFeasibilityResponseProperties",
    "StandardOrderFieldsWithAddons",
    "StandardOrderRequest",
    "StandardOrderRequestProperties",
    "StandardPriceRequestProperties",
    "StandardRequestProperties",
    "StandardStoredFeasibilityRequestProperties",
    "StoredAssuredOrderRequestProperties",
    "StoredFeasibilityFeatureCollection",
    "StoredFeasibilityRequest",
    "StoredOrderResponse",
    "StoredStandardOrderRequestProperties",
    "ValidationError",
    "ValidationErrorDetail",
    "ValidationErrorResponse",
)

# Ensure all Pydantic models have forward refs rebuilt
import inspect
import sys

from pydantic import BaseModel

_current_module = sys.modules[__name__]

for _obj in list(_current_module.__dict__.values()):
    if inspect.isclass(_obj) and issubclass(_obj, BaseModel) and _obj is not BaseModel:
        _obj.model_rebuild()
