# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field


class PointGeometry(BaseModel):
    """GeoJSON Point geometry.

    Represents a single point location in WGS84 coordinates (longitude, latitude).

        Attributes:
            coordinates (list[float | int]): The coordinates of the point as [longitude, latitude].
            type_ (Union[Literal['Point'], None]):  Default: 'Point'.
    """

    coordinates: list[float | int] = Field(
        ...,
        description="""The coordinates of the point as [longitude, latitude].""",
        alias="coordinates",
    )
    type_: Union[Literal["Point"], None] = Field(
        default="Point", description=None, alias="type"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
