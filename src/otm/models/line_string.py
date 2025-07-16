from typing import Literal, Union

from pydantic import BaseModel


class LineString(BaseModel):
    """LineString Model

    Attributes:
        type (Literal['LineString']):
        coordinates (list[list[float]]):
        bbox (Union[None, list[float]]):
    """

    type: Literal["LineString"] = "LineString"
    coordinates: list[list[float]]
    bbox: Union[None, list[float]] = None
