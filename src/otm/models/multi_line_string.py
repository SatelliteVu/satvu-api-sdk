from typing import Literal, Union

from pydantic import BaseModel, Field


class MultiLineString(BaseModel):
    """MultiLineString Model

    Attributes:
        type (Literal['MultiLineString']):
        coordinates (list[list[list[float]]]):
        bbox (Union[None, list[float]]):
    """

    type: Literal["MultiLineString"] = Field("MultiLineString", description=None)
    coordinates: list[list[list[float]]] = Field(..., description=None)
    bbox: Union[None, list[float]] = Field(None, description=None)
