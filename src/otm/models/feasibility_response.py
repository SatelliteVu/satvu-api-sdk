from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel, Field

from ..models.assured_feasibility_response_feature import (
    AssuredFeasibilityResponseFeature,
)
from ..models.feasibility_request_status import FeasibilityRequestStatus
from ..models.link import Link
from ..models.standard_feasibility_response_feature import (
    StandardFeasibilityResponseFeature,
)


class FeasibilityResponse(BaseModel):
    """FeatureCollection model for stored feasibility response

    Attributes:
        type (Literal['FeatureCollection']):
        features (list[Union[AssuredFeasibilityResponseFeature, StandardFeasibilityResponseFeature]]): Properties of the
            feasibility response.
        id (UUID): Feasibility Request ID.
        links (list['Link']): List of link objects to resources and related URLS.
        status (FeasibilityRequestStatus):
        contract_id (UUID): Contract ID.
        bbox (Union[None, list[float]]):
    """

    type: Literal["FeatureCollection"] = Field("FeatureCollection", description=None)
    features: list[
        Union[AssuredFeasibilityResponseFeature, StandardFeasibilityResponseFeature]
    ] = Field(..., description="Properties of the feasibility response.")
    id: UUID = Field(..., description="Feasibility Request ID.")
    links: list["Link"] = Field(
        ..., description="List of link objects to resources and related URLS."
    )
    status: FeasibilityRequestStatus = Field(..., description=None)
    contract_id: UUID = Field(..., description="Contract ID.")
    bbox: Union[None, list[float]] = Field(None, description=None)
