from typing import Literal, Union

from pydantic import BaseModel, Field


class MultiPolygon(BaseModel):
    """MultiPolygon Model

    Attributes:
        type (Literal['MultiPolygon']):
        coordinates (list[list[list[list[float]]]]):
        bbox (Union[None, list[float]]):
    """

    type: Literal["MultiPolygon"] = Field("MultiPolygon", description=None)
    coordinates: list[list[list[list[float]]]] = Field(..., description=None)
    bbox: Union[None, list[float]] = Field(None, description=None)
