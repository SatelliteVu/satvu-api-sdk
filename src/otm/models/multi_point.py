from typing import Literal, Union

from pydantic import BaseModel, Field


class MultiPoint(BaseModel):
    """MultiPoint Model

    Attributes:
        type (Literal['MultiPoint']):
        coordinates (list[list[float]]):
        bbox (Union[None, list[float]]):
    """

    type: Literal["MultiPoint"] = Field("MultiPoint", description=None)
    coordinates: list[list[float]] = Field(..., description=None)
    bbox: Union[None, list[float]] = Field(None, description=None)
