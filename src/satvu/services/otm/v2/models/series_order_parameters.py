# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

import pydantic

from ..models.day_night_mode import DayNightMode


class SeriesOrderParameters(pydantic.BaseModel):
    """Template parameters applied to each child order in the series.

    Attributes:
        licence_level (None | str): The licence level for the order. Licence levels are specific to the contract.
            Defaults to the contract's licence level with the smallest uplift.
        addon_withhold (None | str): How long the order's imagery is withheld from the public catalog, as an ISO 8601
            duration. Withhold options are specific to the contract. Defaults to the contract's default withhold option.
        satvu_day_night_mode (Union[None, 'DayNightMode']):
        max_cloud_cover (Union[None, int]): The maximum acceptable cloud cover. Measured in percent. Must be at least
            25. Default: 25.
        min_off_nadir (Union[None, int]): The minimum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Default: 0.
        max_off_nadir (Union[None, int]): The maximum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Must be greater than `min_off_nadir`. Default: 30.
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
    satvu_day_night_mode: Union[None, DayNightMode] = pydantic.Field(
        default=None, description=None, alias="satvu:day_night_mode"
    )
    max_cloud_cover: Union[None, int] = pydantic.Field(
        default=25,
        description="""The maximum acceptable cloud cover. Measured in percent. Must be at least 25.""",
        alias="max_cloud_cover",
    )
    min_off_nadir: Union[None, int] = pydantic.Field(
        default=0,
        description="""The minimum angle from the sensor between nadir and the scene center. Measured in decimal degrees.""",
        alias="min_off_nadir",
    )
    max_off_nadir: Union[None, int] = pydantic.Field(
        default=30,
        description="""The maximum angle from the sensor between nadir and the scene center. Measured in decimal degrees. Must be greater than `min_off_nadir`.""",
        alias="max_off_nadir",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
