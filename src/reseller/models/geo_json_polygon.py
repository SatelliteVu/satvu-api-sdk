from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.geo_json_polygon_type import GeoJSONPolygonType


class GeoJSONPolygon(BaseModel):
    """
    Attributes:
        type_ ('GeoJSONPolygonType'):
        coordinates (list[list[list[float]]]):
        bbox (Union[None, list[float]]):
    """

    type_: "GeoJSONPolygonType" = Field(..., description=None, alias="type")
    coordinates: list[list[list[float]]] = Field(
        ..., description=None, alias="coordinates"
    )
    bbox: Union[None, list[float]] = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
