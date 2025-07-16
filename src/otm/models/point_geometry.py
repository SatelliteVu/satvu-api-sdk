from typing import Literal, Union

from pydantic import BaseModel, Field


class PointGeometry(BaseModel):
    """
    Attributes:
        coordinates (list[Union[float, int]]): The coordinates of the item.
        type (Union[Literal['Point'], None]):  Default: 'Point'.
    """

    coordinates: list[Union[float, int]] = Field(
        ..., description="The coordinates of the item."
    )
    type: Union[Literal["Point"], None] = Field("Point", description=None)
