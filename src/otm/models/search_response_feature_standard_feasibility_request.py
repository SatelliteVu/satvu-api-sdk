from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel, Field

from ..models.point import Point
from ..models.price import Price
from ..models.standard_stored_feasibility_request_properties import (
    StandardStoredFeasibilityRequestProperties,
)


class SearchResponseFeatureStandardFeasibilityRequest(BaseModel):
    """
    Attributes:
        type (Literal['Feature']):
        geometry (Union[None, Point]):
        properties (Union[None, StandardStoredFeasibilityRequestProperties]):
        id (UUID): ID of an item associated with the search parameters.
        contract_id (UUID): Contract ID associated with the search.
        collection (str): Name of collection associated with the search result item.
        price (Price):
        bbox (Union[None, list[float]]):
    """

    type: Literal["Feature"] = Field("Feature", description=None)
    geometry: Union[None, Point] = Field(..., description=None)
    properties: Union[None, StandardStoredFeasibilityRequestProperties] = Field(
        ..., description=None
    )
    id: UUID = Field(
        ..., description="ID of an item associated with the search parameters."
    )
    contract_id: UUID = Field(
        ..., description="Contract ID associated with the search."
    )
    collection: str = Field(
        ..., description="Name of collection associated with the search result item."
    )
    price: "Price" = Field(..., description=None)
    bbox: Union[None, list[float]] = Field(None, description=None)
