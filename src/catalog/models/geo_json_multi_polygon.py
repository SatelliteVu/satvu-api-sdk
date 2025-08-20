from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.geo_json_multi_polygon_type import GeoJSONMultiPolygonType


class GeoJSONMultiPolygon(BaseModel):
    """
    Attributes:
        type_ (GeoJSONMultiPolygonType):
        coordinates (list[list[list[list[float]]]]):
        bbox (Union[None, list[float]]):
    """

    type_: GeoJSONMultiPolygonType = Field(..., description=None, alias="type")
    coordinates: list[list[list[list[float]]]] = Field(
        ..., description=None, alias="coordinates"
    )
    bbox: Union[None, list[float]] = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
