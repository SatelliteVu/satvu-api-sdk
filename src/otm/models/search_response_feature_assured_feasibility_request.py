from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel

from ..models.assured_stored_feasibility_request_properties import (
    AssuredStoredFeasibilityRequestProperties,
)
from ..models.point import Point
from ..models.price import Price


class SearchResponseFeatureAssuredFeasibilityRequest(BaseModel):
    """
    Attributes:
        type (Literal['Feature']):
        geometry (Union[None, Point]):
        properties (Union[AssuredStoredFeasibilityRequestProperties, None]):
        id (UUID): ID of an item associated with the search parameters.
        contract_id (UUID): Contract ID associated with the search.
        collection (str): Name of collection associated with the search result item.
        price (Price):
        bbox (Union[None, list[float]]):
    """

    type: Literal["Feature"] = "Feature"
    geometry: Union[None, Point]
    properties: Union[AssuredStoredFeasibilityRequestProperties, None]
    id: UUID
    contract_id: UUID
    collection: str
    price: "Price"
    bbox: Union[None, list[float]] = None
