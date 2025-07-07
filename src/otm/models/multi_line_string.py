from typing import Literal, Union

from pydantic import BaseModel


class MultiLineString(BaseModel):
    """MultiLineString Model

    Attributes:
        type (Literal['MultiLineString']):
        coordinates (list[list[list[float]]]):
        bbox (Union[None, list[float]]):
    """

    type: Literal["MultiLineString"]
    coordinates: list[list[list[float]]]
    bbox: Union[None, list[float]] = None
