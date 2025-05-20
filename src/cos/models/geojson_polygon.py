from dataclasses import dataclass
from typing import Literal


@dataclass
class GeojsonPolygon:
    """
    Attributes:
        type (Literal['Polygon']):
        coordinates (list[list[list[float]]]):
    """

    type: Literal["Polygon"]
    coordinates: list[list[list[float]]]

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "type",
            "coordinates",
        }
