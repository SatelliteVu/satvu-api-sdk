# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Literal

import pydantic


class Polygon(pydantic.BaseModel):
    """
    Attributes:
        type_ (Literal['Polygon']):
        coordinates (list[list[list[float]]]):
    """

    type_: Literal["Polygon"] = pydantic.Field(
        default="Polygon", description=None, alias="type"
    )
    coordinates: list[list[list[float]]] = pydantic.Field(
        ..., description=None, alias="coordinates"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
