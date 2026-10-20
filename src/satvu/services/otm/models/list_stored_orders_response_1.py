# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union

import pydantic

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.reseller_stored_order_response import ResellerStoredOrderResponse
    from ..models.response_context import ResponseContext
    from ..models.stored_order_response import StoredOrderResponse


class ListStoredOrdersResponse1(pydantic.BaseModel):
    """
    Attributes:
        type_ (Literal['FeatureCollection']):
        features (list[Union['ResellerStoredOrderResponse', 'StoredOrderResponse']]): List of stored order requests.
        links (list[Link]): Links to previous and/or next page.
        context (ResponseContext): Context about the response.
    """

    type_: Literal["FeatureCollection"] = pydantic.Field(
        default="FeatureCollection", description=None, alias="type"
    )
    features: list[Union[ResellerStoredOrderResponse, StoredOrderResponse]] = (
        pydantic.Field(
            ..., description="""List of stored order requests.""", alias="features"
        )
    )
    links: list[Link] = pydantic.Field(
        ..., description="""Links to previous and/or next page.""", alias="links"
    )
    context: ResponseContext = pydantic.Field(
        ..., description="""Context about the response.""", alias="context"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
