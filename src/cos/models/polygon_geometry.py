from dataclasses import dataclass
from typing import Literal, Union

from ..types import UNSET, Unset


@dataclass
class PolygonGeometry:
    """
    Attributes:
        type (Union[Literal['Polygon'], Unset]):  Default: 'Polygon'.
        coordinates (Union[Unset, list[list[list[Union[float, int]]]]]): The coordinates of the item.
    """

    type: Union[Literal["Polygon"], Unset] = "Polygon"
    coordinates: Union[Unset, list[list[list[Union[float, int]]]]] = UNSET

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {}
