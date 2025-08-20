from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.geo_json_geometry_collection_1_type import GeoJSONGeometryCollection1Type
from ..models.geo_json_line_string import GeoJSONLineString
from ..models.geo_json_multi_line_string import GeoJSONMultiLineString
from ..models.geo_json_multi_point import GeoJSONMultiPoint
from ..models.geo_json_multi_polygon import GeoJSONMultiPolygon
from ..models.geo_json_point import GeoJSONPoint
from ..models.geo_json_polygon import GeoJSONPolygon


class GeoJSONGeometryCollection1(BaseModel):
    """
    Attributes:
        type_ (GeoJSONGeometryCollection1Type):
        geometries (list[Union['GeoJSONLineString', 'GeoJSONMultiLineString', 'GeoJSONMultiPoint',
            'GeoJSONMultiPolygon', 'GeoJSONPoint', 'GeoJSONPolygon']]):
    """

    type_: GeoJSONGeometryCollection1Type = Field(..., description=None, alias="type")
    geometries: list[
        Union[
            "GeoJSONLineString",
            "GeoJSONMultiLineString",
            "GeoJSONMultiPoint",
            "GeoJSONMultiPolygon",
            "GeoJSONPoint",
            "GeoJSONPolygon",
        ]
    ] = Field(..., description=None, alias="geometries")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
