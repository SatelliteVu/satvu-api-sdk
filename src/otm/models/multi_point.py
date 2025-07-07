from typing import Literal, Union

from pydantic import BaseModel


class MultiPoint(BaseModel):
    """MultiPoint Model

    Attributes:
        type (Literal['MultiPoint']):
        coordinates (list[list[float]]):
        bbox (Union[None, list[float]]):
    """

    type: Literal["MultiPoint"]
    coordinates: list[list[float]]
    bbox: Union[None, list[float]] = None
