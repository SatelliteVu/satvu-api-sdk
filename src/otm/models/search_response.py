from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, Union

if TYPE_CHECKING:
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


@dataclass
class SearchResponse:
    """
    Attributes:
        type (Literal['FeatureCollection']):
        features (list[Union['ResellerSearchResponseFeatureAssuredOrderRequest',
            'ResellerSearchResponseFeatureStandardOrderRequest', 'SearchResponseFeatureAssuredFeasibilityRequest',
            'SearchResponseFeatureAssuredFeasibilityResponse', 'SearchResponseFeatureAssuredOrderRequest',
            'SearchResponseFeatureStandardFeasibilityRequest', 'SearchResponseFeatureStandardFeasibilityResponse',
            'SearchResponseFeatureStandardOrderRequest']]): A list of features that match the search filters.
        context (ResponseContext):
        links (list['Link']): A list of links to next and/or previous pages of the search.
        bbox (Union[None, list[float]]):
    """

    type: Literal["FeatureCollection"]
    features: list[
        Union[
            "ResellerSearchResponseFeatureAssuredOrderRequest",
            "ResellerSearchResponseFeatureStandardOrderRequest",
            "SearchResponseFeatureAssuredFeasibilityRequest",
            "SearchResponseFeatureAssuredFeasibilityResponse",
            "SearchResponseFeatureAssuredOrderRequest",
            "SearchResponseFeatureStandardFeasibilityRequest",
            "SearchResponseFeatureStandardFeasibilityResponse",
            "SearchResponseFeatureStandardOrderRequest",
        ]
    ]
    context: "ResponseContext"
    links: list["Link"]
    bbox: Union[None, list[float]] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "type",
            "features",
            "context",
            "links",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "type": object,
            "features": object,
            "context": object,
            "links": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "bbox": object,
        }
