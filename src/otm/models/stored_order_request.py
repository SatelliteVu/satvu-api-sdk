from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel

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

    type: Literal["Feature"]
    geometry: "Point"
    properties: Union[
        StoredAssuredOrderRequestProperties, StoredStandardOrderRequestProperties
    ]
    id: UUID
    links: list["Link"]
    contract_id: UUID
    price: "Price1"
