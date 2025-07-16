from typing import Literal, Union

from pydantic import BaseModel, Field


class LineString(BaseModel):
    """LineString Model

    Attributes:
        type (Literal['LineString']):
        coordinates (list[list[float]]):
        bbox (Union[None, list[float]]):
    """

    type: Literal["LineString"] = Field("LineString", description=None)
    coordinates: list[list[float]] = Field(..., description=None)
    bbox: Union[None, list[float]] = Field(None, description=None)
