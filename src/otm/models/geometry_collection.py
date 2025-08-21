from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.geo_json_line_string import GeoJSONLineString
    from ..models.geo_json_multi_line_string import GeoJSONMultiLineString
    from ..models.geo_json_multi_point import GeoJSONMultiPoint
    from ..models.geo_json_multi_polygon import GeoJSONMultiPolygon
    from ..models.geo_json_point import GeoJSONPoint
    from ..models.geo_json_polygon import GeoJSONPolygon


class GeometryCollection(BaseModel):
    """GeometryCollection Model

    Attributes:
        type_ (Literal['GeometryCollection']):
        geometries (list[Union['GeoJSONLineString', 'GeoJSONMultiLineString', 'GeoJSONMultiPoint',
            'GeoJSONMultiPolygon', 'GeoJSONPoint', 'GeoJSONPolygon', 'GeometryCollection']]):
        bbox (Union[None, list[float]]):
    """

    type_: Literal["GeometryCollection"] = Field(
        "GeometryCollection", description=None, alias="type"
    )
    geometries: list[
        Union[
            "GeoJSONLineString",
            "GeoJSONMultiLineString",
            "GeoJSONMultiPoint",
            "GeoJSONMultiPolygon",
            "GeoJSONPoint",
            "GeoJSONPolygon",
            "GeometryCollection",
        ]
    ] = Field(..., description=None, alias="geometries")
    bbox: Union[None, list[float]] = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
