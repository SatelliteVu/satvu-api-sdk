from typing import Literal

from pydantic import BaseModel


class GeojsonPolygon(BaseModel):
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

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "type": object,
            "coordinates": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
