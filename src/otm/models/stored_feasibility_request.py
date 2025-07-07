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

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "type",
            "geometry",
            "properties",
            "id",
            "links",
            "contract_id",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "type": object,
            "geometry": object,
            "properties": object,
            "id": UUID,
            "links": object,
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
