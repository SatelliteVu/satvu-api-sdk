from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.get_assured_order_properties import GetAssuredOrderProperties
    from ..models.get_standard_order_properties import GetStandardOrderProperties
    from ..models.link import Link
    from ..models.point import Point
    from ..models.price import Price


class GetOrderResponse(BaseModel):
    """Payload for get order response.

    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union['GetAssuredOrderProperties', 'GetStandardOrderProperties']): A map of additional metadata
            about the requested image.
        id (UUID): Order ID
        links (list[Link]): A list of related links for the order.
        contract_id (UUID): Contract ID.
        price (Price):
        bbox (list[float] | None):
    """

    type_: Literal["Feature"] = Field("Feature", description=None, alias="type")
    geometry: "Point" = Field(..., description="Point Model", alias="geometry")
    properties: Union["GetAssuredOrderProperties", "GetStandardOrderProperties"] = (
        Field(
            ...,
            description="A map of additional metadata about the requested image.",
            alias="properties",
        )
    )
    id: UUID = Field(..., description="Order ID", alias="id")
    links: list[Link] = Field(
        ..., description="A list of related links for the order.", alias="links"
    )
    contract_id: UUID = Field(..., description="Contract ID.", alias="contract_id")
    price: "Price" = Field(..., description=None, alias="price")
    bbox: list[float] | None = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
