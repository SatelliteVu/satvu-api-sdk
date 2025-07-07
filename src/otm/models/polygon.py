from typing import Literal, Union

from pydantic import BaseModel


class Polygon(BaseModel):
    """Polygon Model

    Attributes:
        type (Literal['Polygon']):
        coordinates (list[list[list[float]]]):
        bbox (Union[None, list[float]]):
    """

    type: Literal["Polygon"]
    coordinates: list[list[list[float]]]
    bbox: Union[None, list[float]] = None
