# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field


class PolygonGeometry(BaseModel):
    """GeoJSON Polygon geometry.

    Represents a polygon with an outer ring and optional holes.
    Coordinates must be in WGS84 (longitude, latitude) and the outer ring
    must be closed (first and last coordinates must be the same).

        Attributes:
            coordinates (list[list[list[float | int]]]): The coordinates of the polygon. First ring is outer, rest are
                holes.
            type_ (Union[Literal['Polygon'], None]):  Default: 'Polygon'.
    """

    coordinates: list[list[list[float | int]]] = Field(
        ...,
        description="""The coordinates of the polygon. First ring is outer, rest are holes.""",
        alias="coordinates",
    )
    type_: Union[Literal["Polygon"], None] = Field(
        default="Polygon", description=None, alias="type"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
