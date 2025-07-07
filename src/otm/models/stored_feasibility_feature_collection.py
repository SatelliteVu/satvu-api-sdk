from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, Union

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.response_context import ResponseContext
    from ..models.stored_feasibility_request import StoredFeasibilityRequest


@dataclass
class StoredFeasibilityFeatureCollection:
    """
    Attributes:
        type (Literal['FeatureCollection']):
        features (list['StoredFeasibilityRequest']): List of stored feasibility requests.
        links (list['Link']): Links to previous and/or next page.
        context (ResponseContext):
        bbox (Union[None, list[float]]):
    """

    type: Literal["FeatureCollection"]
    features: list["StoredFeasibilityRequest"]
    links: list["Link"]
    context: "ResponseContext"
    bbox: Union[None, list[float]] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "type",
            "features",
            "links",
            "context",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "type": object,
            "features": object,
            "links": object,
            "context": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "bbox": object,
        }
