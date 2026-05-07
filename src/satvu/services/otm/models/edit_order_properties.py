# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.day_night_mode import DayNightMode


class EditOrderProperties(BaseModel):
    """Properties that can be edited in an order.

    All fields are optional - only provided fields will be updated.
    Platform-only parameters (name, withhold, licence_level) can be edited at any time.
    Tasking parameters can only be edited for Standard orders in Created/Staged states.

        Attributes:
            licence_level (None | str): The optional licence level for the order. Licence levels are specific to the
                contract. If not specified, the option will be set to the licence with the smallest uplift in the relevant
                contract.
            addon_withhold (None | str): The optional ISO8601 string describing the duration that an order will be withheld
                from the public catalog. Withhold options are specific to the contract. If not specified, the option will be set
                to the default specified in the relevant contract.
            name (None | str): The name of the order.
            start_time (datetime.datetime | None): The start of the tasking window. Only editable for Standard orders in
                Created/Staged states.
            end_time (datetime.datetime | None): The end of the tasking window. Only editable for Standard orders in
                Created/Staged states.
            satvu_day_night_mode (Union['DayNightMode', None]): The mode of data capture. Only editable for Standard orders
                in Created/Staged states.
            max_cloud_cover (int | None): The max threshold of acceptable cloud coverage. Only editable for Standard orders
                in Created/Staged states.
            min_off_nadir (int | None): The minimum angle from the sensor between nadir and the scene center. Only editable
                for Standard orders in Created/Staged states.
            max_off_nadir (int | None): The maximum angle from the sensor between nadir and the scene center. Only editable
                for Standard orders in Created/Staged states.
    """

    licence_level: None | str = Field(
        default=None,
        description="""The optional licence level for the order. Licence levels are specific to the contract. If not specified, the option will be set to the licence with the smallest uplift in the relevant contract.""",
        alias="licence_level",
    )
    addon_withhold: None | str = Field(
        default=None,
        description="""The optional ISO8601 string describing the duration that an order will be withheld from the public catalog. Withhold options are specific to the contract. If not specified, the option will be set to the default specified in the relevant contract.""",
        alias="addon:withhold",
    )
    name: None | str = Field(
        default=None, description="""The name of the order.""", alias="name"
    )
    start_time: datetime.datetime | None = Field(
        default=None,
        description="""The start of the tasking window. Only editable for Standard orders in Created/Staged states.""",
        alias="start_time",
    )
    end_time: datetime.datetime | None = Field(
        default=None,
        description="""The end of the tasking window. Only editable for Standard orders in Created/Staged states.""",
        alias="end_time",
    )
    satvu_day_night_mode: Union[DayNightMode, None] = Field(
        default=None,
        description="""The mode of data capture. Only editable for Standard orders in Created/Staged states.""",
        alias="satvu:day_night_mode",
    )
    max_cloud_cover: int | None = Field(
        default=None,
        description="""The max threshold of acceptable cloud coverage. Only editable for Standard orders in Created/Staged states.""",
        alias="max_cloud_cover",
    )
    min_off_nadir: int | None = Field(
        default=None,
        description="""The minimum angle from the sensor between nadir and the scene center. Only editable for Standard orders in Created/Staged states.""",
        alias="min_off_nadir",
    )
    max_off_nadir: int | None = Field(
        default=None,
        description="""The maximum angle from the sensor between nadir and the scene center. Only editable for Standard orders in Created/Staged states.""",
        alias="max_off_nadir",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
