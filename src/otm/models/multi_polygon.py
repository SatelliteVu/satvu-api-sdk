from typing import Literal, Union

from pydantic import BaseModel


class MultiPolygon(BaseModel):
    """MultiPolygon Model

    Attributes:
        type (Literal['MultiPolygon']):
        coordinates (list[list[list[list[float]]]]):
        bbox (Union[None, list[float]]):
    """

    type: Literal["MultiPolygon"]
    coordinates: list[list[list[list[float]]]]
    bbox: Union[None, list[float]] = None
