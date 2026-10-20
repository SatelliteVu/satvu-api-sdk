# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

if TYPE_CHECKING:
    from ..models.feature_collection_order import FeatureCollectionOrder
    from ..models.link import Link
    from ..models.reseller_feature_collection_order import (
        ResellerFeatureCollectionOrder,
    )
    from ..models.response_context import ResponseContext


class OrderPage(pydantic.BaseModel):
    """Response payload for querying orders

    Attributes:
        orders (list[Union['FeatureCollectionOrder', 'ResellerFeatureCollectionOrder']]): A list of existing orders
            owned by the user.
        links (list[Link]): A list of links to next and/or previous pages of the query.
        context (ResponseContext): Context about the response.
    """

    orders: list[Union[FeatureCollectionOrder, ResellerFeatureCollectionOrder]] = (
        pydantic.Field(
            ...,
            description="""A list of existing orders owned by the user.""",
            alias="orders",
        )
    )
    links: list[Link] = pydantic.Field(
        ...,
        description="""A list of links to next and/or previous pages of the query.""",
        alias="links",
    )
    context: ResponseContext = pydantic.Field(
        ..., description="""Context about the response.""", alias="context"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
