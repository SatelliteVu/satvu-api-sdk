from typing import Literal, Union

from pydantic import BaseModel

from ..models.line_string import LineString
from ..models.multi_line_string import MultiLineString
from ..models.multi_point import MultiPoint
from ..models.multi_polygon import MultiPolygon
from ..models.point import Point
from ..models.polygon import Polygon


class GeometryCollection(BaseModel):
    """GeometryCollection Model

    Attributes:
        type (Literal['GeometryCollection']):
        geometries (list[Union['GeometryCollection', 'LineString', 'MultiLineString', 'MultiPoint', 'MultiPolygon',
            'Point', 'Polygon']]):
        bbox (Union[None, list[float]]):
    """

    type: Literal["GeometryCollection"] = "GeometryCollection"
    geometries: list[
        Union[
            "GeometryCollection",
            "LineString",
            "MultiLineString",
            "MultiPoint",
            "MultiPolygon",
            "Point",
            "Polygon",
        ]
    ]
    bbox: Union[None, list[float]] = None
