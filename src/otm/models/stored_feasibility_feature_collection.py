from typing import Literal, Union

from pydantic import BaseModel, Field

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

    type: Literal["FeatureCollection"] = Field("FeatureCollection", description=None)
    features: list["StoredFeasibilityRequest"] = Field(
        ..., description="List of stored feasibility requests."
    )
    links: list["Link"] = Field(..., description="Links to previous and/or next page.")
    context: "ResponseContext" = Field(..., description=None)
    bbox: Union[None, list[float]] = Field(None, description=None)
