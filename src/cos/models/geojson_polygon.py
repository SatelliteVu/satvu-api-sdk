from typing import Literal

from pydantic import BaseModel


class GeojsonPolygon(BaseModel):
    """
    Attributes:
        type (Literal['Polygon']):
        coordinates (list[list[list[float]]]):
    """

    type: Literal["Polygon"]
    coordinates: list[list[list[float]]]
