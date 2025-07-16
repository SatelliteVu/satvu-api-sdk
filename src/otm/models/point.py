from typing import Literal, Union

from pydantic import BaseModel


class Point(BaseModel):
    """Point Model

    Attributes:
        type (Literal['Point']):
        coordinates (list[float]):
        bbox (Union[None, list[float]]):
    """

    type: Literal["Point"] = "Point"
    coordinates: list[float]
    bbox: Union[None, list[float]] = None
