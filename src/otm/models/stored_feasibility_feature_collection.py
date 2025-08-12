from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.link import Link
from ..models.response_context import ResponseContext
from ..models.stored_feasibility_request import StoredFeasibilityRequest


class StoredFeasibilityFeatureCollection(BaseModel):
    """
    Attributes:
        type_ (Literal['FeatureCollection']):
        features (list['StoredFeasibilityRequest']): List of stored feasibility requests.
        links (list['Link']): Links to previous and/or next page.
        context (ResponseContext):
        bbox (Union[None, list[float]]):
    """

    type_: Literal["FeatureCollection"] = Field(
        "FeatureCollection", description=None, alias="type"
    )
    features: list["StoredFeasibilityRequest"] = Field(
        ..., description="List of stored feasibility requests.", alias="features"
    )
    links: list["Link"] = Field(
        ..., description="Links to previous and/or next page.", alias="links"
    )
    context: "ResponseContext" = Field(..., description=None, alias="context")
    bbox: Union[None, list[float]] = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
