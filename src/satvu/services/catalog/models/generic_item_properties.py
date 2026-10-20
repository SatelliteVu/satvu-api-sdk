# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import Union

import pydantic


class GenericItemProperties(pydantic.BaseModel):
    """
    Attributes:
        created (datetime.datetime):
        updated (datetime.datetime):
        datetime_ (Union[None, datetime.datetime]):
        eo_cloud_cover (float | None):
        gsd (Union[None, float]):
        platform (Union[None, str]):
        satvu_filter (Union[None, str]):
        satvu_geometric_calibration (Union[None, bool]):
        view_azimuth (Union[None, float]):
        view_off_nadir (Union[None, float]):
        view_sun_azimuth (Union[None, float]):
        view_sun_elevation (Union[None, float]):
    """

    created: datetime.datetime = pydantic.Field(..., description=None, alias="created")
    updated: datetime.datetime = pydantic.Field(..., description=None, alias="updated")
    datetime_: Union[None, datetime.datetime] = pydantic.Field(
        default=None, description=None, alias="datetime"
    )
    eo_cloud_cover: float | None = pydantic.Field(
        default=None, description=None, alias="eo:cloud_cover"
    )
    gsd: Union[None, float] = pydantic.Field(
        default=None, description=None, alias="gsd"
    )
    platform: Union[None, str] = pydantic.Field(
        default=None, description=None, alias="platform"
    )
    satvu_filter: Union[None, str] = pydantic.Field(
        default=None, description=None, alias="satvu:filter"
    )
    satvu_geometric_calibration: Union[None, bool] = pydantic.Field(
        default=None, description=None, alias="satvu:geometric_calibration"
    )
    view_azimuth: Union[None, float] = pydantic.Field(
        default=None, description=None, alias="view:azimuth"
    )
    view_off_nadir: Union[None, float] = pydantic.Field(
        default=None, description=None, alias="view:off_nadir"
    )
    view_sun_azimuth: Union[None, float] = pydantic.Field(
        default=None, description=None, alias="view:sun_azimuth"
    )
    view_sun_elevation: Union[None, float] = pydantic.Field(
        default=None, description=None, alias="view:sun_elevation"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
