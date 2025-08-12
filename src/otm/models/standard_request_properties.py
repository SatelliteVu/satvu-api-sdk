from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.day_night_mode import DayNightMode


class StandardRequestProperties(BaseModel):
    """
    Attributes:
        datetime_ (str): The closed date-time interval of the tasking order request.
        product (Union[Literal['standard'], None]): Standard Priority. Default: 'standard'.
        satvu_day_night_mode (Union[None, DayNightMode]):
        max_cloud_cover (Union[None, int]): The max threshold of acceptable cloud coverage. Measured in percent.
            Default: 15.
        min_off_nadir (Union[None, int]): The minimum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Default: 0.
        max_off_nadir (Union[None, int]): The maximum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Must be larger than `min_off_nadir`. Default: 30.
    """

    datetime_: str = Field(
        ...,
        description="The closed date-time interval of the tasking order request.",
        alias="datetime",
    )
    product: Union[Literal["standard"], None] = Field(
        "standard", description="Standard Priority.", alias="product"
    )
    satvu_day_night_mode: Union[None, DayNightMode] = Field(
        None, description=None, alias="satvu:day_night_mode"
    )
    max_cloud_cover: Union[None, int] = Field(
        15,
        description="The max threshold of acceptable cloud coverage. Measured in percent.",
        alias="max_cloud_cover",
    )
    min_off_nadir: Union[None, int] = Field(
        0,
        description="The minimum angle from the sensor between nadir and the scene center. Measured in decimal degrees.",
        alias="min_off_nadir",
    )
    max_off_nadir: Union[None, int] = Field(
        30,
        description="The maximum angle from the sensor between nadir and the scene center. Measured in decimal degrees. Must be larger than `min_off_nadir`.",
        alias="max_off_nadir",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
