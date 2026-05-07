# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.point import Point


class TaskAcquisition(BaseModel):
    """Acquisition metadata for a task.

    Attributes:
        start_time (datetime.datetime): Start time of the acquisition window.
        end_time (datetime.datetime): End time of the acquisition window.
        geometry (Point): Point Model
        off_nadir (float): Off-nadir angle in degrees.
        sun_el (float): Sun elevation angle in degrees.
        sun_azimuth (float): Sun azimuth angle in degrees.
    """

    start_time: datetime.datetime = Field(
        ..., description="""Start time of the acquisition window.""", alias="start_time"
    )
    end_time: datetime.datetime = Field(
        ..., description="""End time of the acquisition window.""", alias="end_time"
    )
    geometry: Point = Field(..., description="""Point Model""", alias="geometry")
    off_nadir: float = Field(
        ..., description="""Off-nadir angle in degrees.""", alias="off_nadir"
    )
    sun_el: float = Field(
        ..., description="""Sun elevation angle in degrees.""", alias="sun_el"
    )
    sun_azimuth: float = Field(
        ..., description="""Sun azimuth angle in degrees.""", alias="sun_azimuth"
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
