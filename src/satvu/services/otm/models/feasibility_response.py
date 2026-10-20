# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union
from uuid import UUID

import pydantic

from ..models.feasibility_request_status import FeasibilityRequestStatus

if TYPE_CHECKING:
    from ..models.assured_feasibility_response_feature import (
        AssuredFeasibilityResponseFeature,
    )
    from ..models.link import Link
    from ..models.standard_feasibility_response_feature import (
        StandardFeasibilityResponseFeature,
    )


class FeasibilityResponse(pydantic.BaseModel):
    """FeatureCollection model for stored feasibility response

    Attributes:
        type_ (Literal['FeatureCollection']):
        features (list[Union['AssuredFeasibilityResponseFeature', 'StandardFeasibilityResponseFeature']]): Properties of
            the feasibility response.
        id (UUID): Feasibility Request ID.
        links (list[Link]): List of link objects to resources and related URLS.
        status ('FeasibilityRequestStatus'): The status of the feasibility request.
        contract_id (UUID): Contract ID.
    """

    type_: Literal["FeatureCollection"] = pydantic.Field(
        default="FeatureCollection", description=None, alias="type"
    )
    features: list[
        Union[AssuredFeasibilityResponseFeature, StandardFeasibilityResponseFeature]
    ] = pydantic.Field(
        ..., description="""Properties of the feasibility response.""", alias="features"
    )
    id: UUID = pydantic.Field(
        ..., description="""Feasibility Request ID.""", alias="id"
    )
    links: list[Link] = pydantic.Field(
        ...,
        description="""List of link objects to resources and related URLS.""",
        alias="links",
    )
    status: FeasibilityRequestStatus = pydantic.Field(
        ..., description="""The status of the feasibility request.""", alias="status"
    )
    contract_id: UUID = pydantic.Field(
        ..., description="""Contract ID.""", alias="contract_id"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
