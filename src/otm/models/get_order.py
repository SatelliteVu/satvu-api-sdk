from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.geo_json_point import GeoJSONPoint
    from ..models.get_assured_order_properties import GetAssuredOrderProperties
    from ..models.get_standard_order_properties import GetStandardOrderProperties
    from ..models.link import Link
    from ..models.price_1 import Price1


class GetOrder(BaseModel):
    """Feature model for get order request.

    Attributes:
        type_ (Literal['Feature']):
        geometry (GeoJSONPoint):
        properties (Union['GetAssuredOrderProperties', 'GetStandardOrderProperties']): A dictionary of additional
            metadata about the requested image.
        id (UUID): Order ID
        links (list[Link]): A list of related links for the order.
        contract_id (UUID): Contract ID.
        price (Price1):
    """

    type_: Literal["Feature"] = Field("Feature", description=None, alias="type")
    geometry: "GeoJSONPoint" = Field(..., description=None, alias="geometry")
    properties: Union["GetAssuredOrderProperties", "GetStandardOrderProperties"] = (
        Field(
            ...,
            description="A dictionary of additional metadata about the requested image.",
            alias="properties",
        )
    )
    id: UUID = Field(..., description="Order ID", alias="id")
    links: list[Link] = Field(
        ..., description="A list of related links for the order.", alias="links"
    )
    contract_id: UUID = Field(..., description="Contract ID.", alias="contract_id")
    price: "Price1" = Field(..., description=None, alias="price")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
