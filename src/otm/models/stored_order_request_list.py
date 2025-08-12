from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.link import Link
from ..models.reseller_stored_order_request import ResellerStoredOrderRequest
from ..models.response_context import ResponseContext
from ..models.stored_order_request import StoredOrderRequest


class StoredOrderRequestList(BaseModel):
    """
    Attributes:
        type_ (Literal['FeatureCollection']):
        features (list[Union[ResellerStoredOrderRequest, StoredOrderRequest]]): List of stored order requests.
        links (list['Link']): Links to previous and/or next page.
        context (ResponseContext):
    """

    type_: Literal["FeatureCollection"] = Field(
        "FeatureCollection", description=None, alias="type"
    )
    features: list[Union[ResellerStoredOrderRequest, StoredOrderRequest]] = Field(
        ..., description="List of stored order requests.", alias="features"
    )
    links: list["Link"] = Field(
        ..., description="Links to previous and/or next page.", alias="links"
    )
    context: "ResponseContext" = Field(..., description=None, alias="context")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
