# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

if TYPE_CHECKING:
    from ..models.geojson_crs import GeojsonCRS


class GeojsonGeometry(pydantic.BaseModel):
    """Defines the full footprint of the asset represented by the Item, formatted according to RFC 7946 section 3.1.

    Attributes:
        bbox (Union[None, list[float]]):
        coordinates (Union[None, list[float]]):
        crs (Union[None, GeojsonCRS]):
        geometries (Union[None, list[float]]):
        type_ (Union[None, str]):
    """

    bbox: Union[None, list[float]] = pydantic.Field(
        default=None, description=None, alias="bbox"
    )
    coordinates: Union[None, list[float]] = pydantic.Field(
        default=None, description=None, alias="coordinates"
    )
    crs: Union[None, GeojsonCRS] = pydantic.Field(
        default=None, description=None, alias="crs"
    )
    geometries: Union[None, list[float]] = pydantic.Field(
        default=None, description=None, alias="geometries"
    )
    type_: Union[None, str] = pydantic.Field(
        default=None, description=None, alias="type"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
