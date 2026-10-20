# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

import pydantic

from ..models.geo_json_polygon_type import GeoJSONPolygonType


class GeoJSONPolygon(pydantic.BaseModel):
    """
    Attributes:
        type_ ('GeoJSONPolygonType'):
        coordinates (list[list[list[float]]]):
        bbox (Union[None, list[float]]):
    """

    type_: GeoJSONPolygonType = pydantic.Field(..., description=None, alias="type")
    coordinates: list[list[list[float]]] = pydantic.Field(
        ..., description=None, alias="coordinates"
    )
    bbox: Union[None, list[float]] = pydantic.Field(
        default=None, description=None, alias="bbox"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
