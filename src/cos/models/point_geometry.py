from dataclasses import dataclass
from typing import Literal, Union

from ..types import Unset


@dataclass
class PointGeometry:
    """
    Attributes:
        coordinates (list[Union[float, int]]): The coordinates of the item.
        type (Union[Literal['Point'], Unset]):  Default: 'Point'.
    """

    coordinates: list[Union[float, int]]
    type: Union[Literal["Point"], Unset] = "Point"

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "coordinates",
        }
