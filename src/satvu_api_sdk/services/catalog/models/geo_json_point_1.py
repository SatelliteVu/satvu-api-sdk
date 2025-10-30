from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.geo_json_point_1_type import GeoJSONPoint1Type


class GeoJSONPoint1(BaseModel):
    """
    Attributes:
        type_ ('GeoJSONPoint1Type'):
        coordinates (list[float]):
        bbox (Union[None, list[float]]):
    """

    type_: "GeoJSONPoint1Type" = Field(..., description=None, alias="type")
    coordinates: list[float] = Field(..., description=None, alias="coordinates")
    bbox: Union[None, list[float]] = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
