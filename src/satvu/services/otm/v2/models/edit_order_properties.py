# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import Union

import pydantic

from ..models.day_night_mode import DayNightMode


class EditOrderProperties(pydantic.BaseModel):
    """Properties that can be edited in an order.

    All fields are optional - only provided fields will be updated.
    Platform-only parameters (name, withhold, licence_level) can be edited at any time.
    Tasking parameters can only be edited for Standard orders in Created/Staged states.

        Attributes:
            licence_level (None | str): The licence level for the order. Licence levels are specific to the contract.
                Defaults to the contract's licence level with the smallest uplift.
            addon_withhold (None | str): How long the order's imagery is withheld from the public catalog, as an ISO 8601
                duration. Withhold options are specific to the contract. Defaults to the contract's default withhold option.
            name (None | str): The name of the order.
            start_time (datetime.datetime | None): The start of the tasking window. Only editable for standard orders that
                are still `staged`.
            end_time (datetime.datetime | None): The end of the tasking window. Only editable for standard orders that are
                still `staged`.
            satvu_day_night_mode (Union['DayNightMode', None]): The mode of data capture. Only editable for standard orders
                that are still `staged`.
            max_cloud_cover (int | None): The maximum acceptable cloud cover. Measured in percent. Must be at least 25. Only
                editable for standard orders that are still `staged`.
            min_off_nadir (int | None): The minimum angle from the sensor between nadir and the scene center. Only editable
                for standard orders that are still `staged`.
            max_off_nadir (int | None): The maximum angle from the sensor between nadir and the scene center. Only editable
                for standard orders that are still `staged`.
    """

    licence_level: None | str = pydantic.Field(
        default=None,
        description="""The licence level for the order. Licence levels are specific to the contract. Defaults to the contract's licence level with the smallest uplift.""",
        alias="licence_level",
    )
    addon_withhold: None | str = pydantic.Field(
        default=None,
        description="""How long the order's imagery is withheld from the public catalog, as an ISO 8601 duration. Withhold options are specific to the contract. Defaults to the contract's default withhold option.""",
        alias="addon:withhold",
    )
    name: None | str = pydantic.Field(
        default=None, description="""The name of the order.""", alias="name"
    )
    start_time: datetime.datetime | None = pydantic.Field(
        default=None,
        description="""The start of the tasking window. Only editable for standard orders that are still `staged`.""",
        alias="start_time",
    )
    end_time: datetime.datetime | None = pydantic.Field(
        default=None,
        description="""The end of the tasking window. Only editable for standard orders that are still `staged`.""",
        alias="end_time",
    )
    satvu_day_night_mode: Union[DayNightMode, None] = pydantic.Field(
        default=None,
        description="""The mode of data capture. Only editable for standard orders that are still `staged`.""",
        alias="satvu:day_night_mode",
    )
    max_cloud_cover: int | None = pydantic.Field(
        default=None,
        description="""The maximum acceptable cloud cover. Measured in percent. Must be at least 25. Only editable for standard orders that are still `staged`.""",
        alias="max_cloud_cover",
    )
    min_off_nadir: int | None = pydantic.Field(
        default=None,
        description="""The minimum angle from the sensor between nadir and the scene center. Only editable for standard orders that are still `staged`.""",
        alias="min_off_nadir",
    )
    max_off_nadir: int | None = pydantic.Field(
        default=None,
        description="""The maximum angle from the sensor between nadir and the scene center. Only editable for standard orders that are still `staged`.""",
        alias="max_off_nadir",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
