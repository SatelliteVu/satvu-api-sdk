# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Literal

import pydantic


class MultiPolygon(pydantic.BaseModel):
    """MultiPolygon Model

    Attributes:
        type_ (Literal['MultiPolygon']):
        coordinates (list[list[list[list[float]]]]):
        bbox (list[float] | None):
    """

    type_: Literal["MultiPolygon"] = pydantic.Field(
        default="MultiPolygon", description=None, alias="type"
    )
    coordinates: list[list[list[list[float]]]] = pydantic.Field(
        ..., description=None, alias="coordinates"
    )
    bbox: list[float] | None = pydantic.Field(
        default=None, description=None, alias="bbox"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
