# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class GeojsonPolygon(BaseModel):
    """
    Attributes:
        type_ (Literal['Polygon']):
        coordinates (list[list[list[float]]]):
    """

    type_: Literal["Polygon"] = Field(default="Polygon", description=None, alias="type")
    coordinates: list[list[list[float]]] = Field(
        ..., description=None, alias="coordinates"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
