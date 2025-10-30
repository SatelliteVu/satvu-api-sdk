from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.geo_json_polygon_1_type import GeoJSONPolygon1Type


class GeoJSONPolygon1(BaseModel):
    """
    Attributes:
        type_ ('GeoJSONPolygon1Type'):
        coordinates (list[list[list[float]]]):
        bbox (Union[None, list[float]]):
    """

    type_: "GeoJSONPolygon1Type" = Field(..., description=None, alias="type")
    coordinates: list[list[list[float]]] = Field(
        ..., description=None, alias="coordinates"
    )
    bbox: Union[None, list[float]] = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
