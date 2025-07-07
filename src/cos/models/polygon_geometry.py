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
