# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

import pydantic

from ..models.geo_json_point_type import GeoJSONPointType


class GeoJSONPoint(pydantic.BaseModel):
    """
    Attributes:
        type_ ('GeoJSONPointType'):
        coordinates (list[float]):
        bbox (Union[None, list[float]]):
    """

    type_: GeoJSONPointType = pydantic.Field(..., description=None, alias="type")
    coordinates: list[float] = pydantic.Field(
        ..., description=None, alias="coordinates"
    )
    bbox: Union[None, list[float]] = pydantic.Field(
        default=None, description=None, alias="bbox"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
