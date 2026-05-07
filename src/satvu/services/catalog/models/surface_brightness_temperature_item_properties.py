# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class SurfaceBrightnessTemperatureItemProperties(BaseModel):
    """
    Attributes:
        processing_software (Union[None, str]):
        proj_bbox (Union[None, str]):
        proj_epsg (Union[None, float]):
        proj_geometry (Union[None, str]):
        proj_shape (Union[None, str]):
        proj_transform (Union[None, str]):
        satvu_multiframe_stacking (Union[None, bool]):
    """

    processing_software: Union[None, str] = Field(
        default=None, description=None, alias="processing:software"
    )
    proj_bbox: Union[None, str] = Field(
        default=None, description=None, alias="proj:bbox"
    )
    proj_epsg: Union[None, float] = Field(
        default=None, description=None, alias="proj:epsg"
    )
    proj_geometry: Union[None, str] = Field(
        default=None, description=None, alias="proj:geometry"
    )
    proj_shape: Union[None, str] = Field(
        default=None, description=None, alias="proj:shape"
    )
    proj_transform: Union[None, str] = Field(
        default=None, description=None, alias="proj:transform"
    )
    satvu_multiframe_stacking: Union[None, bool] = Field(
        default=None, description=None, alias="satvu:multiframe_stacking"
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
