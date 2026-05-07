# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, Literal, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.line_string import LineString
    from ..models.multi_line_string import MultiLineString
    from ..models.multi_point import MultiPoint
    from ..models.multi_polygon import MultiPolygon
    from ..models.point import Point
    from ..models.polygon import Polygon


class GeometryCollection(BaseModel):
    """GeometryCollection Model

    Attributes:
        type_ (Literal['GeometryCollection']):
        geometries (list[Union['GeometryCollection', 'LineString', 'MultiLineString', 'MultiPoint', 'MultiPolygon',
            'Point', 'Polygon']]):
        bbox (list[float] | None):
    """

    type_: Literal["GeometryCollection"] = Field(
        default="GeometryCollection", description=None, alias="type"
    )
    geometries: list[
        Annotated[
            Union[
                GeometryCollection,
                LineString,
                MultiLineString,
                MultiPoint,
                MultiPolygon,
                Point,
                Polygon,
            ],
            Field(discriminator="type_"),
        ]
    ] = Field(..., description=None, alias="geometries")
    bbox: list[float] | None = Field(default=None, description=None, alias="bbox")

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
