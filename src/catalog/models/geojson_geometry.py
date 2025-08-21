from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from typing import Union

    from ..models.geojson_crs import GeojsonCRS


class GeojsonGeometry(BaseModel):
    """Defines the full footprint of the asset represented by the Item, formatted according to RFC 7946 section 3.1.

    Attributes:
        bbox (Union[None, list[int]]):
        coordinates (Union[None, list[int]]):
        crs (Union[None, GeojsonCRS]):
        geometries (Union[None, list[int]]):
        type_ (Union[None, str]):
    """

    bbox: Union[None, list[int]] = Field(None, description=None, alias="bbox")
    coordinates: Union[None, list[int]] = Field(
        None, description=None, alias="coordinates"
    )
    crs: Union[None, "GeojsonCRS"] = Field(None, description=None, alias="crs")
    geometries: Union[None, list[int]] = Field(
        None, description=None, alias="geometries"
    )
    type_: Union[None, str] = Field(None, description=None, alias="type")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
