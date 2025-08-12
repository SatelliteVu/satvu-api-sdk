from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from ..models.point import Point
from ..models.price import Price
from ..models.search_standard_order_properties import SearchStandardOrderProperties


class SearchResponseFeatureStandardOrderRequest(BaseModel):
    """
    Attributes:
        type_ (Literal['Feature']):
        geometry (Union[None, Point]):
        properties (Union[None, SearchStandardOrderProperties]):
        id (UUID): ID of an item associated with the search parameters.
        contract_id (UUID): Contract ID associated with the search.
        collection (str): Name of collection associated with the search result item.
        price (Price):
        bbox (Union[None, list[float]]):
    """

    type_: Literal["Feature"] = Field("Feature", description=None, alias="type")
    geometry: Union[None, Point] = Field(..., description=None, alias="geometry")
    properties: Union[None, SearchStandardOrderProperties] = Field(
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

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
