from __future__ import annotations

from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field


class PolygonGeometry(BaseModel):
    """
    Attributes:
        type_ (Union[Literal['Polygon'], None]):  Default: 'Polygon'.
        coordinates (Union[None, list[list[list[Union[float, int]]]]]): The coordinates of the item.
    """

    type_: Union[Literal["Polygon"], None] = Field(
        "Polygon", description=None, alias="type"
    )
    coordinates: Union[None, list[list[list[Union[float, int]]]]] = Field(
        None, description="The coordinates of the item.", alias="coordinates"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
