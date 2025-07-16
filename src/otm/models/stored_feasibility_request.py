from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel, Field

from ..models.assured_stored_feasibility_request_properties import (
    AssuredStoredFeasibilityRequestProperties,
)
from ..models.link import Link
from ..models.point import Point
from ..models.standard_stored_feasibility_request_properties import (
    StandardStoredFeasibilityRequestProperties,
)


class StoredFeasibilityRequest(BaseModel):
    """Object representing a stored feasibility request.

    Attributes:
        type (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union[AssuredStoredFeasibilityRequestProperties, StandardStoredFeasibilityRequestProperties]): A
            dictionary of additional metadata about the requested image.
        id (UUID): Feasibility Request ID.
        links (list['Link']): A list of related links for the feasibility request.
        contract_id (UUID): Contract ID.
        bbox (Union[None, list[float]]):
    """

    type: Literal["Feature"] = Field("Feature", description=None)
    geometry: "Point" = Field(..., description="Point Model")
    properties: Union[
        AssuredStoredFeasibilityRequestProperties,
        StandardStoredFeasibilityRequestProperties,
    ] = Field(
        ...,
        description="A dictionary of additional metadata about the requested image.",
    )
    id: UUID = Field(..., description="Feasibility Request ID.")
    links: list["Link"] = Field(
        ..., description="A list of related links for the feasibility request."
    )
    contract_id: UUID = Field(..., description="Contract ID.")
    bbox: Union[None, list[float]] = Field(None, description=None)
