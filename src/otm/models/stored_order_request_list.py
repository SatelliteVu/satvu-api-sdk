from typing import Literal, Union

from pydantic import BaseModel, Field

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

    type: Literal["FeatureCollection"] = Field("FeatureCollection", description=None)
    features: list[Union[ResellerStoredOrderRequest, StoredOrderRequest]] = Field(
        ..., description="List of stored order requests."
    )
    links: list["Link"] = Field(..., description="Links to previous and/or next page.")
    context: "ResponseContext" = Field(..., description=None)
