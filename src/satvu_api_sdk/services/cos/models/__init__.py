"""Contains all the data models used in inputs/outputs"""

from .download_order_get_collections_type_0_item import (
    DownloadOrderGetCollectionsType0Item,
)
from .feature_collection_order import FeatureCollectionOrder
from .feature_collection_order_1 import FeatureCollectionOrder1
from .feature_order import FeatureOrder
from .feature_order_1 import FeatureOrder1
from .geojson_polygon import GeojsonPolygon
from .geojson_polygon_1 import GeojsonPolygon1
from .http_exception_response import HttpExceptionResponse
from .http_validation_error import HTTPValidationError
from .link import Link
from .link_body_type_0 import LinkBodyType0
from .link_method import LinkMethod
from .order import Order
from .order_1 import Order1
from .order_download_url import OrderDownloadUrl
from .order_edit_payload import OrderEditPayload
from .order_item_download_url import OrderItemDownloadUrl
from .order_page import OrderPage
from .order_submission_payload import OrderSubmissionPayload
from .point_geometry import PointGeometry
from .polygon import Polygon
from .polygon_1 import Polygon1
from .polygon_2 import Polygon2
from .polygon_3 import Polygon3
from .polygon_geometry import PolygonGeometry
from .price import Price
from .reseller_feature_collection_order import ResellerFeatureCollectionOrder
from .reseller_feature_collection_order_1 import ResellerFeatureCollectionOrder1
from .reseller_submission_order_payload import ResellerSubmissionOrderPayload
from .response_context import ResponseContext
from .satvu_filter import SatvuFilter
from .search_request import SearchRequest
from .stac_metadata import StacMetadata
from .stac_metadata_1 import StacMetadata1
from .stac_metadata_1_assets import StacMetadata1Assets
from .stac_metadata_assets import StacMetadataAssets
from .stac_properties_v4 import StacPropertiesV4
from .stac_properties_v7 import StacPropertiesV7
from .stac_properties_v7_processing_software_name_version import (
    StacPropertiesV7ProcessingSoftwareNameVersion,
)
from .stac_properties_v8 import StacPropertiesV8
from .stac_properties_v8_processing_software_name_version import (
    StacPropertiesV8ProcessingSoftwareNameVersion,
)
from .stac_properties_v41 import StacPropertiesV41
from .stac_properties_v71 import StacPropertiesV71
from .stac_properties_v71_processing_software_name_version import (
    StacPropertiesV71ProcessingSoftwareNameVersion,
)
from .stac_properties_v81 import StacPropertiesV81
from .stac_properties_v81_processing_software_name_version import (
    StacPropertiesV81ProcessingSoftwareNameVersion,
)
from .validation_error import ValidationError

__all__ = (
    "DownloadOrderGetCollectionsType0Item",
    "FeatureCollectionOrder",
    "FeatureCollectionOrder1",
    "FeatureOrder",
    "FeatureOrder1",
    "GeojsonPolygon",
    "GeojsonPolygon1",
    "HttpExceptionResponse",
    "HTTPValidationError",
    "Link",
    "LinkBodyType0",
    "LinkMethod",
    "Order",
    "Order1",
    "OrderDownloadUrl",
    "OrderEditPayload",
    "OrderItemDownloadUrl",
    "OrderPage",
    "OrderSubmissionPayload",
    "PointGeometry",
    "Polygon",
    "Polygon1",
    "Polygon2",
    "Polygon3",
    "PolygonGeometry",
    "Price",
    "ResellerFeatureCollectionOrder",
    "ResellerFeatureCollectionOrder1",
    "ResellerSubmissionOrderPayload",
    "ResponseContext",
    "SatvuFilter",
    "SearchRequest",
    "StacMetadata",
    "StacMetadata1",
    "StacMetadata1Assets",
    "StacMetadataAssets",
    "StacPropertiesV4",
    "StacPropertiesV41",
    "StacPropertiesV7",
    "StacPropertiesV71",
    "StacPropertiesV71ProcessingSoftwareNameVersion",
    "StacPropertiesV7ProcessingSoftwareNameVersion",
    "StacPropertiesV8",
    "StacPropertiesV81",
    "StacPropertiesV81ProcessingSoftwareNameVersion",
    "StacPropertiesV8ProcessingSoftwareNameVersion",
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
