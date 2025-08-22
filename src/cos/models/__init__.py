"""Contains all the data models used in inputs/outputs"""

from .download_order_collections_type_0_item import DownloadOrderCollectionsType0Item
from .feature_collection_order import FeatureCollectionOrder
from .feature_order import FeatureOrder
from .geojson_polygon import GeojsonPolygon
from .http_exception_response import HttpExceptionResponse
from .http_validation_error import HTTPValidationError
from .link import Link
from .link_body_type_0 import LinkBodyType0
from .link_method import LinkMethod
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
from .validation_error import ValidationError

__all__ = (
    "DownloadOrderCollectionsType0Item",
    "FeatureCollectionOrder",
    "FeatureOrder",
    "GeojsonPolygon",
    "HttpExceptionResponse",
    "HTTPValidationError",
    "Link",
    "LinkBodyType0",
    "LinkMethod",
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
