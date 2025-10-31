from __future__ import annotations

import datetime

from pydantic import BaseModel, ConfigDict, Field


class Outage(BaseModel):
    """Model representing a satellite outage.

    Attributes:
        satellite_code (str): The satellite affected by the outage.
        start_time (datetime.datetime): The start datetime of the outage.
        end_time (datetime.datetime): The end datetime of the outage.
    """

    satellite_code: str = Field(
        ..., description="The satellite affected by the outage.", alias="satellite_code"
    )
    start_time: datetime.datetime = Field(
        ..., description="The start datetime of the outage.", alias="start_time"
    )
    end_time: datetime.datetime = Field(
        ..., description="The end datetime of the outage.", alias="end_time"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
