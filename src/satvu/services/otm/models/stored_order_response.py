# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, Literal, Union
from uuid import UUID

import pydantic

from satvu.shared.discriminators import const_tag

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.point import Point
    from ..models.price import Price
    from ..models.stored_assured_order_request_properties import (
        StoredAssuredOrderRequestProperties,
    )
    from ..models.stored_standard_order_request_properties import (
        StoredStandardOrderRequestProperties,
    )


class StoredOrderResponse(pydantic.BaseModel):
    """Payload for stored order response.

    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union['StoredAssuredOrderRequestProperties', 'StoredStandardOrderRequestProperties']): A map of
            additional metadata about the requested image.
        id (UUID): Order ID.
        links (list[Link]): A list of related links for the order.
        contract_id (UUID): Contract ID.
        price (Price):
        series_id (None | UUID): ID of the recurring order series this order belongs to.
    """

    type_: Literal["Feature"] = pydantic.Field(
        default="Feature", description=None, alias="type"
    )
    geometry: Point = pydantic.Field(
        ..., description="""Point Model""", alias="geometry"
    )
    properties: Annotated[
        Union[
            Annotated[StoredAssuredOrderRequestProperties, pydantic.Tag("assured")],
            Annotated[StoredStandardOrderRequestProperties, pydantic.Tag("standard")],
        ],
        pydantic.Discriminator(const_tag("product", default="standard")),
    ] = pydantic.Field(
        ...,
        description="""A map of additional metadata about the requested image.""",
        alias="properties",
    )
    id: UUID = pydantic.Field(..., description="""Order ID.""", alias="id")
    links: list[Link] = pydantic.Field(
        ..., description="""A list of related links for the order.""", alias="links"
    )
    contract_id: UUID = pydantic.Field(
        ..., description="""Contract ID.""", alias="contract_id"
    )
    price: Price = pydantic.Field(..., description=None, alias="price")
    series_id: None | UUID = pydantic.Field(
        default=None,
        description="""ID of the recurring order series this order belongs to.""",
        alias="series_id",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
