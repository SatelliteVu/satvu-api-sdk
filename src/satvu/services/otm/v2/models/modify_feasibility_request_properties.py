# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

import pydantic

from ..models.day_night_mode import DayNightMode


class ModifyFeasibilityRequestProperties(pydantic.BaseModel):
    """Properties for modify feasibility request.
    All fields are optional - unspecified fields will be sourced from the existing order.
    Only supports Standard product (Assured orders do not support modifications).

        Attributes:
            datetime_ (None | str): The tasking window after the modification, as an ISO 8601 interval (`start/end`). Both
                bounds are required. The start may be in the past and the end less than 7 days away, but the window must be at
                least 7 days long.
            satvu_day_night_mode (Union['DayNightMode', None]): The mode of data capture.
            max_cloud_cover (int | None): The maximum acceptable cloud cover. Measured in percent. Must be at least 25.
            min_off_nadir (int | None): The minimum angle from the sensor between nadir and the scene center. Measured in
                decimal degrees.
            max_off_nadir (int | None): The maximum angle from the sensor between nadir and the scene center. Measured in
                decimal degrees. Must be greater than `min_off_nadir`.
    """

    datetime_: None | str = pydantic.Field(
        default=None,
        description="""The tasking window after the modification, as an ISO 8601 interval (`start/end`). Both bounds are required. The start may be in the past and the end less than 7 days away, but the window must be at least 7 days long.""",
        alias="datetime",
    )
    satvu_day_night_mode: Union[DayNightMode, None] = pydantic.Field(
        default=None,
        description="""The mode of data capture.""",
        alias="satvu:day_night_mode",
    )
    max_cloud_cover: int | None = pydantic.Field(
        default=None,
        description="""The maximum acceptable cloud cover. Measured in percent. Must be at least 25.""",
        alias="max_cloud_cover",
    )
    min_off_nadir: int | None = pydantic.Field(
        default=None,
        description="""The minimum angle from the sensor between nadir and the scene center. Measured in decimal degrees.""",
        alias="min_off_nadir",
    )
    max_off_nadir: int | None = pydantic.Field(
        default=None,
        description="""The maximum angle from the sensor between nadir and the scene center. Measured in decimal degrees. Must be greater than `min_off_nadir`.""",
        alias="max_off_nadir",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
