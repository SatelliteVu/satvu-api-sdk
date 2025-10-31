from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class MultiPoint(BaseModel):
    """MultiPoint Model

    Attributes:
        type_ (Literal['MultiPoint']):
        coordinates (list[list[float]]):
        bbox (list[float] | None):
    """

    type_: Literal["MultiPoint"] = Field("MultiPoint", description=None, alias="type")
    coordinates: list[list[float]] = Field(..., description=None, alias="coordinates")
    bbox: list[float] | None = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
