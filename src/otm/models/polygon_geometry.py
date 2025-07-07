from typing import Literal, Union

from pydantic import BaseModel


class PolygonGeometry(BaseModel):
    """
    Attributes:
        type (Union[Literal['Polygon'], None]):  Default: 'Polygon'.
        coordinates (Union[None, list[list[list[Union[float, int]]]]]): The coordinates of the item.
    """

    type: Union[Literal["Polygon"], None] = "Polygon"
    coordinates: Union[None, list[list[list[Union[float, int]]]]] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {}

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {}

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "type": object,
            "coordinates": object,
        }
