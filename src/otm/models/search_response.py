from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field

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
        type_ (Literal['FeatureCollection']):
        features (list[Union[ResellerSearchResponseFeatureAssuredOrderRequest,
            ResellerSearchResponseFeatureStandardOrderRequest, SearchResponseFeatureAssuredFeasibilityRequest,
            SearchResponseFeatureAssuredFeasibilityResponse, SearchResponseFeatureAssuredOrderRequest,
            SearchResponseFeatureStandardFeasibilityRequest, SearchResponseFeatureStandardFeasibilityResponse,
            SearchResponseFeatureStandardOrderRequest]]): A list of features that match the search filters.
        context (ResponseContext):
        links (list['Link']): A list of links to next and/or previous pages of the search.
        bbox (Union[None, list[float]]):
    """

    type_: Literal["FeatureCollection"] = Field(
        "FeatureCollection", description=None, alias="type"
    )
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
    ] = Field(
        ...,
        description="A list of features that match the search filters.",
        alias="features",
    )
    context: "ResponseContext" = Field(..., description=None, alias="context")
    links: list["Link"] = Field(
        ...,
        description="A list of links to next and/or previous pages of the search.",
        alias="links",
    )
    bbox: Union[None, list[float]] = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
