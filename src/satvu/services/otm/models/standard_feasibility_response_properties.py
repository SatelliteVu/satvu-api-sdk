# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Literal, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.day_night_mode import DayNightMode

if TYPE_CHECKING:
    from ..models.price import Price


class StandardFeasibilityResponseProperties(BaseModel):
    """Properties of the standard priority feasibility response.

    Attributes:
        datetime_ (str): The closed date-time interval of the tasking order request.
        created_at (datetime.datetime): The datetime at which the feasibility response was created.
        updated_at (datetime.datetime): The datetime at which the feasibility response was last updated.
        satvu_day_night_mode (Union[None, 'DayNightMode']):
        max_cloud_cover (Union[None, int]): The max threshold of acceptable cloud coverage. Measured in percent.
            Default: 25.
        min_off_nadir (Union[None, int]): The minimum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Default: 0.
        max_off_nadir (Union[None, int]): The maximum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Must be larger than `min_off_nadir`. Default: 30.
        product (Literal['standard']): Standard Priority. Default: 'standard'.
        price (Union['Price', None]): Pricing information.
        min_sun_el (float | None): The minimum sun elevation angle of the pass. Measured in decimal degrees from the
            horizontal.
        max_sun_el (float | None): The maximum sun elevation angle of the pass. Measured in decimal degrees from the
            horizontal.
        min_gsd (float | None): The minimum ground sample distance value of the pass. Measured in metres representing
            the square root of the area of the pixel size projected onto the earth.
        max_gsd (float | None): The maximum ground sample distance value of the pass. Measured in metres representing
            the square root of the area of the pixel size projected onto the earth.
    """

    datetime_: str = Field(
        ...,
        description="""The closed date-time interval of the tasking order request.""",
        alias="datetime",
    )
    created_at: datetime.datetime = Field(
        ...,
        description="""The datetime at which the feasibility response was created.""",
        alias="created_at",
    )
    updated_at: datetime.datetime = Field(
        ...,
        description="""The datetime at which the feasibility response was last updated.""",
        alias="updated_at",
    )
    satvu_day_night_mode: Union[None, DayNightMode] = Field(
        default=None, description=None, alias="satvu:day_night_mode"
    )
    max_cloud_cover: Union[None, int] = Field(
        default=25,
        description="""The max threshold of acceptable cloud coverage. Measured in percent.""",
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
    price: Union[Price, None] = Field(
        default=None, description="""Pricing information.""", alias="price"
    )
    min_sun_el: float | None = Field(
        default=None,
        description="""The minimum sun elevation angle of the pass. Measured in decimal degrees from the horizontal.""",
        alias="min_sun_el",
    )
    max_sun_el: float | None = Field(
        default=None,
        description="""The maximum sun elevation angle of the pass. Measured in decimal degrees from the horizontal.""",
        alias="max_sun_el",
    )
    min_gsd: float | None = Field(
        default=None,
        description="""The minimum ground sample distance value of the pass. Measured in metres representing the square root of the area of the pixel size projected onto the earth.""",
        alias="min_gsd",
    )
    max_gsd: float | None = Field(
        default=None,
        description="""The maximum ground sample distance value of the pass. Measured in metres representing the square root of the area of the pixel size projected onto the earth.""",
        alias="max_gsd",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
