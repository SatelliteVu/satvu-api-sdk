from typing import Literal, Union

from pydantic import BaseModel, Field


class PolygonGeometry(BaseModel):
    """
    Attributes:
        type (Union[Literal['Polygon'], None]):  Default: 'Polygon'.
        coordinates (Union[None, list[list[list[Union[float, int]]]]]): The coordinates of the item.
    """

    type: Union[Literal["Polygon"], None] = Field("Polygon", description=None)
    coordinates: Union[None, list[list[list[Union[float, int]]]]] = Field(
        None, description="The coordinates of the item."
    )
