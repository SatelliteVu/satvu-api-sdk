# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

import pydantic

from ..models.geo_json_multi_polygon_type import GeoJSONMultiPolygonType


class GeoJSONMultiPolygon(pydantic.BaseModel):
    """
    Attributes:
        type_ ('GeoJSONMultiPolygonType'):
        coordinates (list[list[list[list[float]]]]):
        bbox (Union[None, list[float]]):
    """

    type_: GeoJSONMultiPolygonType = pydantic.Field(..., description=None, alias="type")
    coordinates: list[list[list[list[float]]]] = pydantic.Field(
        ..., description=None, alias="coordinates"
    )
    bbox: Union[None, list[float]] = pydantic.Field(
        default=None, description=None, alias="bbox"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
