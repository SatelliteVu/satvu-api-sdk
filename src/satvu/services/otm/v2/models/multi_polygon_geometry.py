# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Literal

import pydantic


class MultiPolygonGeometry(pydantic.BaseModel):
    """GeoJSON MultiPolygon geometry.

    Represents a collection of polygons. Commonly produced when a footprint
    crosses the antimeridian and is split into multiple polygons. Coordinates
    must be in WGS84 (longitude, latitude); each polygon's outer ring must be
    closed (first and last coordinates must be the same).

        Attributes:
            coordinates (list[list[list[list[float | int]]]]): The coordinates of the multipolygon. Each element is a
                polygon (list of rings); the first ring is the outer boundary, the rest are holes.
            type_ (Literal['MultiPolygon']):  Default: 'MultiPolygon'.
    """

    coordinates: list[list[list[list[float | int]]]] = pydantic.Field(
        ...,
        description="""The coordinates of the multipolygon. Each element is a polygon (list of rings); the first ring is the outer boundary, the rest are holes.""",
        alias="coordinates",
    )
    type_: Literal["MultiPolygon"] = pydantic.Field(
        default="MultiPolygon", description=None, alias="type"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
