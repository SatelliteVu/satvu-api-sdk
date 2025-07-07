from typing import Literal, Union

from pydantic import BaseModel


class PointGeometry(BaseModel):
    """
    Attributes:
        coordinates (list[Union[float, int]]): The coordinates of the item.
        type (Union[Literal['Point'], None]):  Default: 'Point'.
    """

    coordinates: list[Union[float, int]]
    type: Union[Literal["Point"], None] = "Point"

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "coordinates",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "coordinates": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "type": object,
        }
