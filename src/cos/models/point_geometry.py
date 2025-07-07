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
