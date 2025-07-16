from typing import Literal, Union

from pydantic import BaseModel, Field


class Polygon(BaseModel):
    """Polygon Model

    Attributes:
        type (Literal['Polygon']):
        coordinates (list[list[list[float]]]):
        bbox (Union[None, list[float]]):
    """

    type: Literal["Polygon"] = Field("Polygon", description=None)
    coordinates: list[list[list[float]]] = Field(..., description=None)
    bbox: Union[None, list[float]] = Field(None, description=None)
