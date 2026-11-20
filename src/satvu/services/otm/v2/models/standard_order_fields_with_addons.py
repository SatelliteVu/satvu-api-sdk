# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Literal, Union

import pydantic

from ..models.day_night_mode import DayNightMode


class StandardOrderFieldsWithAddons(pydantic.BaseModel):
    """The parameters of the standard order the price was calculated for.

    Attributes:
        datetime_ (str): The tasking window: the interval within which the order may be acquired, as an ISO 8601
            interval (`start/end`). Both bounds are required.
        licence_level (None | str): The licence level for the order. Licence levels are specific to the contract.
        addon_withhold (None | str): How long the order's imagery is withheld from the public catalog, as an ISO 8601
            duration. Withhold options are specific to the contract.
        satvu_day_night_mode (Union[None, 'DayNightMode']): When the satellite may image: by day, by night, or either.
        max_cloud_cover (Union[None, int]): The maximum acceptable cloud cover. Measured in percent. Default: 25.
        min_off_nadir (Union[None, int]): The minimum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Default: 0.
        max_off_nadir (Union[None, int]): The maximum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Must be greater than `min_off_nadir`. Default: 30.
        product (Literal['standard']): The tasking product. Always `standard` (Standard tasking). Default: 'standard'.
    """

    datetime_: str = pydantic.Field(
        ...,
        description="""The tasking window: the interval within which the order may be acquired, as an ISO 8601 interval (`start/end`). Both bounds are required.""",
        alias="datetime",
    )
    licence_level: None | str = pydantic.Field(
        default=None,
        description="""The licence level for the order. Licence levels are specific to the contract.""",
        alias="licence_level",
    )
    addon_withhold: None | str = pydantic.Field(
        default=None,
        description="""How long the order's imagery is withheld from the public catalog, as an ISO 8601 duration. Withhold options are specific to the contract.""",
        alias="addon:withhold",
    )
    satvu_day_night_mode: Union[None, DayNightMode] = pydantic.Field(
        default=None,
        description="""When the satellite may image: by day, by night, or either.""",
        alias="satvu:day_night_mode",
    )
    max_cloud_cover: Union[None, int] = pydantic.Field(
        default=25,
        description="""The maximum acceptable cloud cover. Measured in percent.""",
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
    product: Literal["standard"] = pydantic.Field(
        default="standard",
        description="""The tasking product. Always `standard` (Standard tasking).""",
        alias="product",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
