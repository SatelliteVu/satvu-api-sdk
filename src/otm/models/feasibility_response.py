from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, Union
from uuid import UUID

from ..models.feasibility_request_status import FeasibilityRequestStatus

if TYPE_CHECKING:
    from ..models.assured_feasibility_response_feature import (
        AssuredFeasibilityResponseFeature,
    )
    from ..models.link import Link
    from ..models.standard_feasibility_response_feature import (
        StandardFeasibilityResponseFeature,
    )


@dataclass
class FeasibilityResponse:
    """FeatureCollection model for stored feasibility response

    Attributes:
        type (Literal['FeatureCollection']):
        features (list[Union['AssuredFeasibilityResponseFeature', 'StandardFeasibilityResponseFeature']]): Properties of
            the feasibility response.
        id (UUID): Feasibility Request ID.
        links (list['Link']): List of link objects to resources and related URLS.
        status (FeasibilityRequestStatus):
        contract_id (UUID): Contract ID.
        bbox (Union[None, list[float]]):
    """

    type: Literal["FeatureCollection"]
    features: list[
        Union["AssuredFeasibilityResponseFeature", "StandardFeasibilityResponseFeature"]
    ]
    id: UUID
    links: list["Link"]
    status: FeasibilityRequestStatus
    contract_id: UUID
    bbox: Union[None, list[float]] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "type",
            "features",
            "id",
            "links",
            "status",
            "contract_id",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "type": object,
            "features": object,
            "id": UUID,
            "links": object,
            "status": object,
            "contract_id": UUID,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "bbox": object,
        }
