from __future__ import annotations

from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field


class PointGeometry(BaseModel):
    """
    Attributes:
        coordinates (list[float | int]): The coordinates of the item.
        type_ (Union[Literal['Point'], None]):  Default: 'Point'.
    """

    coordinates: list[float | int] = Field(
        ..., description="The coordinates of the item.", alias="coordinates"
    )
    type_: Union[Literal["Point"], None] = Field(
        "Point", description=None, alias="type"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
