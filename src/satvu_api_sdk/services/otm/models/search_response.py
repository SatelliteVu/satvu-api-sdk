from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.reseller_search_response_feature_assured_order_request_1 import (
        ResellerSearchResponseFeatureAssuredOrderRequest1,
    )
    from ..models.reseller_search_response_feature_standard_order_request_1 import (
        ResellerSearchResponseFeatureStandardOrderRequest1,
    )
    from ..models.response_context import ResponseContext
    from ..models.search_response_feature_assured_feasibility_request_1 import (
        SearchResponseFeatureAssuredFeasibilityRequest1,
    )
    from ..models.search_response_feature_assured_feasibility_response_1 import (
        SearchResponseFeatureAssuredFeasibilityResponse1,
    )
    from ..models.search_response_feature_assured_order_request_1 import (
        SearchResponseFeatureAssuredOrderRequest1,
    )
    from ..models.search_response_feature_standard_feasibility_request_1 import (
        SearchResponseFeatureStandardFeasibilityRequest1,
    )
    from ..models.search_response_feature_standard_feasibility_response_1 import (
        SearchResponseFeatureStandardFeasibilityResponse1,
    )
    from ..models.search_response_feature_standard_order_request_1 import (
        SearchResponseFeatureStandardOrderRequest1,
    )


class SearchResponse(BaseModel):
    """
    Attributes:
        type_ (Literal['FeatureCollection']):
        features (list[Union['ResellerSearchResponseFeatureAssuredOrderRequest1',
            'ResellerSearchResponseFeatureStandardOrderRequest1', 'SearchResponseFeatureAssuredFeasibilityRequest1',
            'SearchResponseFeatureAssuredFeasibilityResponse1', 'SearchResponseFeatureAssuredOrderRequest1',
            'SearchResponseFeatureStandardFeasibilityRequest1', 'SearchResponseFeatureStandardFeasibilityResponse1',
            'SearchResponseFeatureStandardOrderRequest1']]): A list of features that match the search filters.
        context (ResponseContext): Context about the response.
        links (list[Link]): A list of links to next and/or previous pages of the search.
        bbox (list[float] | None):
    """

    type_: Literal["FeatureCollection"] = Field(
        "FeatureCollection", description=None, alias="type"
    )
    features: list[
        Union[
            "ResellerSearchResponseFeatureAssuredOrderRequest1",
            "ResellerSearchResponseFeatureStandardOrderRequest1",
            "SearchResponseFeatureAssuredFeasibilityRequest1",
            "SearchResponseFeatureAssuredFeasibilityResponse1",
            "SearchResponseFeatureAssuredOrderRequest1",
            "SearchResponseFeatureStandardFeasibilityRequest1",
            "SearchResponseFeatureStandardFeasibilityResponse1",
            "SearchResponseFeatureStandardOrderRequest1",
        ]
    ] = Field(
        ...,
        description="A list of features that match the search filters.",
        alias="features",
    )
    context: "ResponseContext" = Field(
        ..., description="Context about the response.", alias="context"
    )
    links: list[Link] = Field(
        ...,
        description="A list of links to next and/or previous pages of the search.",
        alias="links",
    )
    bbox: list[float] | None = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
