from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.day_night_mode import DayNightMode


class ModifyFeasibilityRequestProperties(BaseModel):
    """Properties for modify feasibility request.
    All fields are optional - unspecified fields will be sourced from the existing order.
    Only supports Standard product (Assured orders do not support modifications).

        Attributes:
            datetime_ (None | str): The closed date-time interval of the modified tasking order request. Start date can be
                in the past, end date can be less than 7 days in the future, but minimum 7-day window must be maintained.
            satvu_day_night_mode (Union['DayNightMode', None]): The mode of data capture.
            max_cloud_cover (int | None): The max threshold of acceptable cloud coverage. Measured in percent.
            min_off_nadir (int | None): The minimum angle from the sensor between nadir and the scene center. Measured in
                decimal degrees.
            max_off_nadir (int | None): The maximum angle from the sensor between nadir and the scene center. Measured in
                decimal degrees. Must be larger than `min_off_nadir`.
    """

    datetime_: None | str = Field(
        None,
        description="The closed date-time interval of the modified tasking order request. Start date can be in the past, end date can be less than 7 days in the future, but minimum 7-day window must be maintained.",
        alias="datetime",
    )
    satvu_day_night_mode: Union["DayNightMode", None] = Field(
        None, description="The mode of data capture.", alias="satvu:day_night_mode"
    )
    max_cloud_cover: int | None = Field(
        None,
        description="The max threshold of acceptable cloud coverage. Measured in percent.",
        alias="max_cloud_cover",
    )
    min_off_nadir: int | None = Field(
        None,
        description="The minimum angle from the sensor between nadir and the scene center. Measured in decimal degrees.",
        alias="min_off_nadir",
    )
    max_off_nadir: int | None = Field(
        None,
        description="The maximum angle from the sensor between nadir and the scene center. Measured in decimal degrees. Must be larger than `min_off_nadir`.",
        alias="max_off_nadir",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
