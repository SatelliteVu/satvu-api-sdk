from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel

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

    type: Literal["Feature"]
    geometry: "Point"
    properties: Union[
        AssuredStoredFeasibilityRequestProperties,
        StandardStoredFeasibilityRequestProperties,
    ]
    id: UUID
    links: list["Link"]
    contract_id: UUID
    bbox: Union[None, list[float]] = None
