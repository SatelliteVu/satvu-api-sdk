from typing import Literal, TypedDict, Union

from ..types import Unset


class PointGeometry(TypedDict):
    """
    Attributes:
        coordinates (list[Union[float, int]]): The coordinates of the item.
        type_ (Union[Literal['Point'], Unset]):  Default: 'Point'.
    """

    coordinates: list[Union[float, int]]
    type_: Union[Literal["Point"], Unset] = "Point"
