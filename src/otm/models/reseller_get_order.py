from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel

from ..models.get_assured_order_properties import GetAssuredOrderProperties
from ..models.get_standard_order_properties import GetStandardOrderProperties
from ..models.link import Link
from ..models.point import Point
from ..models.price_1 import Price1


class ResellerGetOrder(BaseModel):
    """
    Attributes:
        type (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union[GetAssuredOrderProperties, GetStandardOrderProperties]): A dictionary of additional metadata
            about the requested image.
        id (UUID): Order ID
        links (list['Link']): A list of related links for the order.
        contract_id (UUID): Contract ID.
        price (Price1):
        reseller_end_user_id (UUID):
    """

    type: Literal["Feature"]
    geometry: "Point"
    properties: Union[GetAssuredOrderProperties, GetStandardOrderProperties]
    id: UUID
    links: list["Link"]
    contract_id: UUID
    price: "Price1"
    reseller_end_user_id: UUID
