from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.point import Point
    from ..models.price import Price
    from ..models.search_assured_order_properties import SearchAssuredOrderProperties


class SearchResponseFeatureAssuredOrderRequest(BaseModel):
    """
    Attributes:
        type_ (Literal['Feature']):
        geometry (Union['Point', None]):
        properties (Union['SearchAssuredOrderProperties', None]):
        id (UUID): ID of an item associated with the search parameters.
        contract_id (UUID): Contract ID associated with the search.
        collection (str): Name of collection associated with the search result item.
        price (Price):
        bbox (Union[None, list[float]]):
        links (Union[None, list[Link]]): A list of links to the STAC item that fulfilled the order, if applicable.
    """

    type_: Literal["Feature"] = Field("Feature", description=None, alias="type")
    geometry: Union["Point", None] = Field(..., description=None, alias="geometry")
    properties: Union["SearchAssuredOrderProperties", None] = Field(
        ..., description=None, alias="properties"
    )
    id: UUID = Field(
        ...,
        description="ID of an item associated with the search parameters.",
        alias="id",
    )
    contract_id: UUID = Field(
        ..., description="Contract ID associated with the search.", alias="contract_id"
    )
    collection: str = Field(
        ...,
        description="Name of collection associated with the search result item.",
        alias="collection",
    )
    price: "Price" = Field(..., description=None, alias="price")
    bbox: Union[None, list[float]] = Field(None, description=None, alias="bbox")
    links: Union[None, list[Link]] = Field(
        None,
        description="A list of links to the STAC item that fulfilled the order, if applicable.",
        alias="links",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
