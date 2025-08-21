from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.geo_json_point import GeoJSONPoint
    from ..models.link import Link
    from ..models.price import Price
    from ..models.standard_feasibility_response_properties import (
        StandardFeasibilityResponseProperties,
    )


class SearchResponseFeatureStandardFeasibilityResponse(BaseModel):
    """
    Attributes:
        type_ (Literal['Feature']):
        geometry (Union['GeoJSONPoint', None]):
        properties (Union['StandardFeasibilityResponseProperties', None]):
        id (UUID): ID of an item associated with the search parameters.
        contract_id (UUID): Contract ID associated with the search.
        collection (str): Name of collection associated with the search result item.
        price (Price):
        bbox (Union[None, list[float]]):
        links (Union[None, list[Link]]): A list of links to the STAC item that fulfilled the order, if applicable.
    """

    type_: Literal["Feature"] = Field("Feature", description=None, alias="type")
    geometry: Union["GeoJSONPoint", None] = Field(
        ..., description=None, alias="geometry"
    )
    properties: Union["StandardFeasibilityResponseProperties", None] = Field(
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
