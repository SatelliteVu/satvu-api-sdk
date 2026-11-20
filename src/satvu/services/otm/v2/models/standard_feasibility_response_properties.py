# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Literal, Union

import pydantic

from ..models.day_night_mode import DayNightMode

if TYPE_CHECKING:
    from ..models.price import Price


class StandardFeasibilityResponseProperties(pydantic.BaseModel):
    """The properties of the result of a standard feasibility request.

    Attributes:
        datetime_ (str): The tasking window: the interval within which the order may be acquired, as an ISO 8601
            interval (`start/end`). Both bounds are required.
        created_at (datetime.datetime): When the feasibility response was created.
        updated_at (datetime.datetime): When the feasibility response was last updated.
        satvu_day_night_mode (Union[None, 'DayNightMode']): When the satellite may image: by day, by night, or either.
        max_cloud_cover (Union[None, int]): The maximum acceptable cloud cover. Measured in percent. Default: 25.
        min_off_nadir (Union[None, int]): The minimum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Default: 0.
        max_off_nadir (Union[None, int]): The maximum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Must be greater than `min_off_nadir`. Default: 30.
        product (Literal['standard']): The tasking product. Always `standard` (Standard tasking). Default: 'standard'.
        price (Union['Price', None]): Pricing information.
        min_sun_el (float | None): The minimum sun elevation angle. For Assured tasking, the estimate for the pass; for
            Standard tasking, the lowest that `satvu:day_night_mode` allows. Measured in decimal degrees from the
            horizontal.
        max_sun_el (float | None): The maximum sun elevation angle. For Assured tasking, the estimate for the pass; for
            Standard tasking, the highest that `satvu:day_night_mode` allows. Measured in decimal degrees from the
            horizontal.
        min_gsd (float | None): The minimum ground sample distance. For Assured tasking, the estimate for the pass; for
            Standard tasking, the lowest that may be delivered. Measured in meters, as the square root of the pixel area
            projected onto Earth.
        max_gsd (float | None): The maximum ground sample distance. For Assured tasking, the estimate for the pass; for
            Standard tasking, the highest that may be delivered. Measured in meters, as the square root of the pixel area
            projected onto Earth.
    """

    datetime_: str = pydantic.Field(
        ...,
        description="""The tasking window: the interval within which the order may be acquired, as an ISO 8601 interval (`start/end`). Both bounds are required.""",
        alias="datetime",
    )
    created_at: datetime.datetime = pydantic.Field(
        ...,
        description="""When the feasibility response was created.""",
        alias="created_at",
    )
    updated_at: datetime.datetime = pydantic.Field(
        ...,
        description="""When the feasibility response was last updated.""",
        alias="updated_at",
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
    price: Union[Price, None] = pydantic.Field(
        default=None, description="""Pricing information.""", alias="price"
    )
    min_sun_el: float | None = pydantic.Field(
        default=None,
        description="""The minimum sun elevation angle. For Assured tasking, the estimate for the pass; for Standard tasking, the lowest that `satvu:day_night_mode` allows. Measured in decimal degrees from the horizontal.""",
        alias="min_sun_el",
    )
    max_sun_el: float | None = pydantic.Field(
        default=None,
        description="""The maximum sun elevation angle. For Assured tasking, the estimate for the pass; for Standard tasking, the highest that `satvu:day_night_mode` allows. Measured in decimal degrees from the horizontal.""",
        alias="max_sun_el",
    )
    min_gsd: float | None = pydantic.Field(
        default=None,
        description="""The minimum ground sample distance. For Assured tasking, the estimate for the pass; for Standard tasking, the lowest that may be delivered. Measured in meters, as the square root of the pixel area projected onto Earth.""",
        alias="min_gsd",
    )
    max_gsd: float | None = pydantic.Field(
        default=None,
        description="""The maximum ground sample distance. For Assured tasking, the estimate for the pass; for Standard tasking, the highest that may be delivered. Measured in meters, as the square root of the pixel area projected onto Earth.""",
        alias="max_gsd",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
