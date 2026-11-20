# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal, Union
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
    """The response to a feasibility request.

    Attributes:
        type_ (Literal['FeatureCollection']):
        features (list[Union['AssuredFeasibilityResponseFeature', 'StandardFeasibilityResponseFeature']]): The
            feasibility results, as GeoJSON features: one per pass for Assured tasking, or a single feature covering the
            tasking window for Standard tasking. Empty when the request is not feasible.
        id (UUID): The ID of the feasibility request.
        links (list[Link]): List of link objects to resources and related URLS.
        status ('FeasibilityRequestStatus'): The status of the feasibility request.
        contract_id (UUID): The ID of the contract.
    """

    type_: Literal["FeatureCollection"] = pydantic.Field(
        default="FeatureCollection", description=None, alias="type"
    )
    features: list[
        Union[AssuredFeasibilityResponseFeature, StandardFeasibilityResponseFeature]
    ] = pydantic.Field(
        ...,
        description="""The feasibility results, as GeoJSON features: one per pass for Assured tasking, or a single feature covering the tasking window for Standard tasking. Empty when the request is not feasible.""",
        alias="features",
    )
    id: UUID = pydantic.Field(
        ..., description="""The ID of the feasibility request.""", alias="id"
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
        ..., description="""The ID of the contract.""", alias="contract_id"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )

    def model_post_init(self, context: Any, /) -> None:
        # Required fields the SDK fills in (constants, spec defaults) must survive
        # model_dump(exclude_unset=True)
        self.__pydantic_fields_set__ = self.model_fields_set.union(["type_"])
