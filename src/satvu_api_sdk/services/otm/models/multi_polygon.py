from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class MultiPolygon(BaseModel):
    """MultiPolygon Model

    Attributes:
        type_ (Literal['MultiPolygon']):
        coordinates (list[list[list[list[float]]]]):
        bbox (list[float] | None):
    """

    type_: Literal["MultiPolygon"] = Field(
        "MultiPolygon", description=None, alias="type"
    )
    coordinates: list[list[list[list[float]]]] = Field(
        ..., description=None, alias="coordinates"
    )
    bbox: list[float] | None = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
