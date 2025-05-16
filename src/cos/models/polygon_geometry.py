from typing import Literal, TypedDict, Union

from ..types import UNSET, Unset


class PolygonGeometry(TypedDict):
    """
    Attributes:
        type_ (Union[Literal['Polygon'], Unset]):  Default: 'Polygon'.
        coordinates (Union[Unset, list[list[list[Union[float, int]]]]]): The coordinates of the item.
    """

    type_: Union[Literal["Polygon"], Unset] = "Polygon"
    coordinates: Union[Unset, list[list[list[Union[float, int]]]]] = UNSET
