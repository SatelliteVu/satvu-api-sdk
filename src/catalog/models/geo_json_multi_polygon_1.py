from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from typing import Union

    from ..models.geo_json_multi_polygon_1_type import GeoJSONMultiPolygon1Type


class GeoJSONMultiPolygon1(BaseModel):
    """
    Attributes:
        type_ (GeoJSONMultiPolygon1Type):
        coordinates (list[list[list[list[float]]]]):
        bbox (Union[None, list[float]]):
    """

    type_: GeoJSONMultiPolygon1Type = Field(..., description=None, alias="type")
    coordinates: list[list[list[list[float]]]] = Field(
        ..., description=None, alias="coordinates"
    )
    bbox: Union[None, list[float]] = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
