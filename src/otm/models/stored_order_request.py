from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel, Field

from ..models.link import Link
from ..models.point import Point
from ..models.price_1 import Price1
from ..models.stored_assured_order_request_properties import (
    StoredAssuredOrderRequestProperties,
)
from ..models.stored_standard_order_request_properties import (
    StoredStandardOrderRequestProperties,
)


class StoredOrderRequest(BaseModel):
    """Feature model for stored order request.

    Attributes:
        type (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union[StoredAssuredOrderRequestProperties, StoredStandardOrderRequestProperties]): A dictionary of
            additional metadata about the requested image.
        id (UUID): Order ID
        links (list['Link']): A list of related links for the order.
        contract_id (UUID): Contract ID.
        price (Price1):
    """

    type: Literal["Feature"] = Field("Feature", description=None)
    geometry: "Point" = Field(..., description="Point Model")
    properties: Union[
        StoredAssuredOrderRequestProperties, StoredStandardOrderRequestProperties
    ] = Field(
        ...,
        description="A dictionary of additional metadata about the requested image.",
    )
    id: UUID = Field(..., description="Order ID")
    links: list["Link"] = Field(
        ..., description="A list of related links for the order."
    )
    contract_id: UUID = Field(..., description="Contract ID.")
    price: "Price1" = Field(..., description=None)
