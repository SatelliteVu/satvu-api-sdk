# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.day_night_mode import DayNightMode


class StoredSeriesOrderParameters(BaseModel):
    """Order parameters as stored on a series and returned in responses.

    Extends the request parameters with `product`, which is set server-side
    (always ``standard``) rather than provided by the requester.

        Attributes:
            licence_level (None | str): The optional licence level for the order. Licence levels are specific to the
                contract. If not specified, the option will be set to the licence with the smallest uplift in the relevant
                contract.
            addon_withhold (None | str): The optional ISO8601 string describing the duration that an order will be withheld
                from the public catalog. Withhold options are specific to the contract. If not specified, the option will be set
                to the default specified in the relevant contract.
            satvu_day_night_mode (Union[None, 'DayNightMode']):
            max_cloud_cover (Union[None, int]): The max threshold of acceptable cloud coverage where the lower limit is
                capped to 25%. Measured in percent. Default: 25.
            min_off_nadir (Union[None, int]): The minimum angle from the sensor between nadir and the scene center. Measured
                in decimal degrees. Default: 0.
            max_off_nadir (Union[None, int]): The maximum angle from the sensor between nadir and the scene center. Measured
                in decimal degrees. Must be larger than `min_off_nadir`. Default: 30.
            product (Literal['standard']): Standard Priority. Default: 'standard'.
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
    satvu_day_night_mode: Union[None, DayNightMode] = Field(
        default=None, description=None, alias="satvu:day_night_mode"
    )
    max_cloud_cover: Union[None, int] = Field(
        default=25,
        description="""The max threshold of acceptable cloud coverage where the lower limit is capped to 25%. Measured in percent.""",
        alias="max_cloud_cover",
    )
    min_off_nadir: Union[None, int] = Field(
        default=0,
        description="""The minimum angle from the sensor between nadir and the scene center. Measured in decimal degrees.""",
        alias="min_off_nadir",
    )
    max_off_nadir: Union[None, int] = Field(
        default=30,
        description="""The maximum angle from the sensor between nadir and the scene center. Measured in decimal degrees. Must be larger than `min_off_nadir`.""",
        alias="max_off_nadir",
    )
    product: Literal["standard"] = Field(
        default="standard", description="""Standard Priority.""", alias="product"
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
