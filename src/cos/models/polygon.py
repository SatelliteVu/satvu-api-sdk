from typing import Literal

from pydantic import BaseModel, Field


class Polygon(BaseModel):
    """
    Attributes:
        type (Literal['Polygon']):
        coordinates (list[list[list[float]]]):
    """

    type: Literal["Polygon"] = Field("Polygon", description=None)
    coordinates: list[list[list[float]]] = Field(..., description=None)
