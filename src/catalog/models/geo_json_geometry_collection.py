from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from typing import Union

    from ..models.geo_json_geometry_collection_type import GeoJSONGeometryCollectionType
    from ..models.geo_json_line_string_1 import GeoJSONLineString1
    from ..models.geo_json_multi_line_string_1 import GeoJSONMultiLineString1
    from ..models.geo_json_multi_point_1 import GeoJSONMultiPoint1
    from ..models.geo_json_multi_polygon_1 import GeoJSONMultiPolygon1
    from ..models.geo_json_point_1 import GeoJSONPoint1
    from ..models.geo_json_polygon_1 import GeoJSONPolygon1


class GeoJSONGeometryCollection(BaseModel):
    """
    Attributes:
        type_ (GeoJSONGeometryCollectionType):
        geometries (list[Union['GeoJSONLineString1', 'GeoJSONMultiLineString1', 'GeoJSONMultiPoint1',
            'GeoJSONMultiPolygon1', 'GeoJSONPoint1', 'GeoJSONPolygon1']]):
    """

    type_: GeoJSONGeometryCollectionType = Field(..., description=None, alias="type")
    geometries: list[
        Union[
            "GeoJSONLineString1",
            "GeoJSONMultiLineString1",
            "GeoJSONMultiPoint1",
            "GeoJSONMultiPolygon1",
            "GeoJSONPoint1",
            "GeoJSONPolygon1",
        ]
    ] = Field(..., description=None, alias="geometries")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
