from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from typing import Union

    from ..models.geo_json_point_type import GeoJSONPointType


class GeoJSONPoint(BaseModel):
    """
    Attributes:
        type_ (GeoJSONPointType):
        coordinates (list[float]):
        bbox (Union[None, list[float]]):
    """

    type_: GeoJSONPointType = Field(..., description=None, alias="type")
    coordinates: list[float] = Field(..., description=None, alias="coordinates")
    bbox: Union[None, list[float]] = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
