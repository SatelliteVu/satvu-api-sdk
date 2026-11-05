# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, Any, Literal, Union

import pydantic

if TYPE_CHECKING:
    from ..models.line_string import LineString
    from ..models.multi_line_string import MultiLineString
    from ..models.multi_point import MultiPoint
    from ..models.multi_polygon import MultiPolygon
    from ..models.point import Point
    from ..models.polygon import Polygon


class GeometryCollection(pydantic.BaseModel):
    """GeometryCollection Model

    Attributes:
        type_ (Literal['GeometryCollection']):
        geometries (list[Union['GeometryCollection', 'LineString', 'MultiLineString', 'MultiPoint', 'MultiPolygon',
            'Point', 'Polygon']]):
        bbox (list[float] | None):
    """

    type_: Literal["GeometryCollection"] = pydantic.Field(
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
            pydantic.Field(discriminator="type_"),
        ]
    ] = pydantic.Field(..., description=None, alias="geometries")
    bbox: list[float] | None = pydantic.Field(
        default=None, description=None, alias="bbox"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )

    def model_post_init(self, context: Any, /) -> None:
        # Required fields the SDK fills in (constants, spec defaults) must survive
        # model_dump(exclude_unset=True)
        self.__pydantic_fields_set__ = self.model_fields_set.union(["type_"])
