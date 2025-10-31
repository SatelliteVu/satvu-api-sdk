from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from ..models.feasibility_request_status import FeasibilityRequestStatus

if TYPE_CHECKING:
    from ..models.assured_feasibility_response_feature_1 import (
        AssuredFeasibilityResponseFeature1,
    )
    from ..models.link import Link
    from ..models.standard_feasibility_response_feature_1 import (
        StandardFeasibilityResponseFeature1,
    )


class FeasibilityResponse(BaseModel):
    """FeatureCollection model for stored feasibility response

    Attributes:
        type_ (Literal['FeatureCollection']):
        features (list[Union['AssuredFeasibilityResponseFeature1', 'StandardFeasibilityResponseFeature1']]): Properties
            of the feasibility response.
        id (UUID): Feasibility Request ID.
        links (list[Link]): List of link objects to resources and related URLS.
        status ('FeasibilityRequestStatus'): The status of the feasibility request.
        contract_id (UUID): Contract ID.
        bbox (list[float] | None):
    """

    type_: Literal["FeatureCollection"] = Field(
        "FeatureCollection", description=None, alias="type"
    )
    features: list[
        Union[
            "AssuredFeasibilityResponseFeature1", "StandardFeasibilityResponseFeature1"
        ]
    ] = Field(
        ..., description="Properties of the feasibility response.", alias="features"
    )
    id: UUID = Field(..., description="Feasibility Request ID.", alias="id")
    links: list[Link] = Field(
        ...,
        description="List of link objects to resources and related URLS.",
        alias="links",
    )
    status: "FeasibilityRequestStatus" = Field(
        ..., description="The status of the feasibility request.", alias="status"
    )
    contract_id: UUID = Field(..., description="Contract ID.", alias="contract_id")
    bbox: list[float] | None = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
