# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class GenericItemProperties(BaseModel):
    """
    Attributes:
        datetime_ (Union[None, datetime.datetime]):
        eo_cloud_cover (Union[None, float]):
        gsd (Union[None, float]):
        platform (Union[None, str]):
        satvu_filter (Union[None, str]):
        view_azimuth (Union[None, float]):
        view_off_nadir (Union[None, float]):
        view_sun_azimuth (Union[None, float]):
        view_sun_elevation (Union[None, float]):
    """

    datetime_: Union[None, datetime.datetime] = Field(
        default=None, description=None, alias="datetime"
    )
    eo_cloud_cover: Union[None, float] = Field(
        default=None, description=None, alias="eo:cloud_cover"
    )
    gsd: Union[None, float] = Field(default=None, description=None, alias="gsd")
    platform: Union[None, str] = Field(default=None, description=None, alias="platform")
    satvu_filter: Union[None, str] = Field(
        default=None, description=None, alias="satvu:filter"
    )
    view_azimuth: Union[None, float] = Field(
        default=None, description=None, alias="view:azimuth"
    )
    view_off_nadir: Union[None, float] = Field(
        default=None, description=None, alias="view:off_nadir"
    )
    view_sun_azimuth: Union[None, float] = Field(
        default=None, description=None, alias="view:sun_azimuth"
    )
    view_sun_elevation: Union[None, float] = Field(
        default=None, description=None, alias="view:sun_elevation"
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
