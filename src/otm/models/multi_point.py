from dataclasses import dataclass
from typing import Literal, Union


@dataclass
class MultiPoint:
    """MultiPoint Model

    Attributes:
        type (Literal['MultiPoint']):
        coordinates (list[list[float]]):
        bbox (Union[None, list[float]]):
    """

    type: Literal["MultiPoint"]
    coordinates: list[list[float]]
    bbox: Union[None, list[float]] = None

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
        return {
            "bbox": object,
        }
