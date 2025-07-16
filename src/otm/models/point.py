from typing import Literal, Union

from pydantic import BaseModel, Field


class Point(BaseModel):
    """Point Model

    Attributes:
        type (Literal['Point']):
        coordinates (list[float]):
        bbox (Union[None, list[float]]):
    """

    type: Literal["Point"] = Field("Point", description=None)
    coordinates: list[float] = Field(..., description=None)
    bbox: Union[None, list[float]] = Field(None, description=None)
