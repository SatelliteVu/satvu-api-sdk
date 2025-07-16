from typing import Literal, Union

from pydantic import BaseModel

from ..models.link import Link
from ..models.reseller_stored_order_request import ResellerStoredOrderRequest
from ..models.response_context import ResponseContext
from ..models.stored_order_request import StoredOrderRequest


class StoredOrderRequestList(BaseModel):
    """
    Attributes:
        type (Literal['FeatureCollection']):
        features (list[Union[ResellerStoredOrderRequest, StoredOrderRequest]]): List of stored order requests.
        links (list['Link']): Links to previous and/or next page.
        context (ResponseContext):
    """

    type: Literal["FeatureCollection"] = "FeatureCollection"
    features: list[Union[ResellerStoredOrderRequest, StoredOrderRequest]]
    links: list["Link"]
    context: "ResponseContext"
