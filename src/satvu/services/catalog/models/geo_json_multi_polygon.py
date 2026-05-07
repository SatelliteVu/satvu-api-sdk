# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.geo_json_multi_polygon_type import GeoJSONMultiPolygonType


class GeoJSONMultiPolygon(BaseModel):
    """
    Attributes:
        type_ ('GeoJSONMultiPolygonType'):
        coordinates (list[list[list[list[float]]]]):
        bbox (Union[None, list[float]]):
    """

    type_: GeoJSONMultiPolygonType = Field(..., description=None, alias="type")
    coordinates: list[list[list[list[float]]]] = Field(
        ..., description=None, alias="coordinates"
    )
    bbox: Union[None, list[float]] = Field(default=None, description=None, alias="bbox")

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
