from typing import Literal, Union

from pydantic import BaseModel, Field

from ..models.link import Link
from ..models.reseller_search_response_feature_assured_order_request import (
    ResellerSearchResponseFeatureAssuredOrderRequest,
)
from ..models.reseller_search_response_feature_standard_order_request import (
    ResellerSearchResponseFeatureStandardOrderRequest,
)
from ..models.response_context import ResponseContext
from ..models.search_response_feature_assured_feasibility_request import (
    SearchResponseFeatureAssuredFeasibilityRequest,
)
from ..models.search_response_feature_assured_feasibility_response import (
    SearchResponseFeatureAssuredFeasibilityResponse,
)
from ..models.search_response_feature_assured_order_request import (
    SearchResponseFeatureAssuredOrderRequest,
)
from ..models.search_response_feature_standard_feasibility_request import (
    SearchResponseFeatureStandardFeasibilityRequest,
)
from ..models.search_response_feature_standard_feasibility_response import (
    SearchResponseFeatureStandardFeasibilityResponse,
)
from ..models.search_response_feature_standard_order_request import (
    SearchResponseFeatureStandardOrderRequest,
)


class SearchResponse(BaseModel):
    """
    Attributes:
        type (Literal['FeatureCollection']):
        features (list[Union[ResellerSearchResponseFeatureAssuredOrderRequest,
            ResellerSearchResponseFeatureStandardOrderRequest, SearchResponseFeatureAssuredFeasibilityRequest,
            SearchResponseFeatureAssuredFeasibilityResponse, SearchResponseFeatureAssuredOrderRequest,
            SearchResponseFeatureStandardFeasibilityRequest, SearchResponseFeatureStandardFeasibilityResponse,
            SearchResponseFeatureStandardOrderRequest]]): A list of features that match the search filters.
        context (ResponseContext):
        links (list['Link']): A list of links to next and/or previous pages of the search.
        bbox (Union[None, list[float]]):
    """

    type: Literal["FeatureCollection"] = Field("FeatureCollection", description=None)
    features: list[
        Union[
            ResellerSearchResponseFeatureAssuredOrderRequest,
            ResellerSearchResponseFeatureStandardOrderRequest,
            SearchResponseFeatureAssuredFeasibilityRequest,
            SearchResponseFeatureAssuredFeasibilityResponse,
            SearchResponseFeatureAssuredOrderRequest,
            SearchResponseFeatureStandardFeasibilityRequest,
            SearchResponseFeatureStandardFeasibilityResponse,
            SearchResponseFeatureStandardOrderRequest,
        ]
    ] = Field(..., description="A list of features that match the search filters.")
    context: "ResponseContext" = Field(..., description=None)
    links: list["Link"] = Field(
        ..., description="A list of links to next and/or previous pages of the search."
    )
    bbox: Union[None, list[float]] = Field(None, description=None)
