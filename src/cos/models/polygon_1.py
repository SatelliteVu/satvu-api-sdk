from typing import Literal

from pydantic import BaseModel


class Polygon1(BaseModel):
    """
    Attributes:
        type (Literal['Polygon']):
        coordinates (list[list[list[float]]]):
    """

    type: Literal["Polygon"] = "Polygon"
    coordinates: list[list[list[float]]]
