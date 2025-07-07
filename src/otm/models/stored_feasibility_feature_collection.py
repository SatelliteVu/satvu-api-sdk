from typing import Literal, Union

from pydantic import BaseModel

from ..models.link import Link
from ..models.response_context import ResponseContext
from ..models.stored_feasibility_request import StoredFeasibilityRequest


class StoredFeasibilityFeatureCollection(BaseModel):
    """
    Attributes:
        type (Literal['FeatureCollection']):
        features (list['StoredFeasibilityRequest']): List of stored feasibility requests.
        links (list['Link']): Links to previous and/or next page.
        context (ResponseContext):
        bbox (Union[None, list[float]]):
    """

    type: Literal["FeatureCollection"]
    features: list["StoredFeasibilityRequest"]
    links: list["Link"]
    context: "ResponseContext"
    bbox: Union[None, list[float]] = None
