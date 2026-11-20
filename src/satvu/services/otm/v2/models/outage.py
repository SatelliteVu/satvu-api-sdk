# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime

import pydantic


class Outage(pydantic.BaseModel):
    """A period when a satellite cannot image.

    Attributes:
        satellite_name (str): The satellite affected by the outage.
        start_time (datetime.datetime): When the outage starts.
        end_time (datetime.datetime): When the outage ends.
    """

    satellite_name: str = pydantic.Field(
        ...,
        description="""The satellite affected by the outage.""",
        alias="satellite_name",
    )
    start_time: datetime.datetime = pydantic.Field(
        ..., description="""When the outage starts.""", alias="start_time"
    )
    end_time: datetime.datetime = pydantic.Field(
        ..., description="""When the outage ends.""", alias="end_time"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
