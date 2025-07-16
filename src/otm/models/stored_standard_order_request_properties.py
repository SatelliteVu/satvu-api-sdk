from typing import Literal, Union

from pydantic import BaseModel, Field

from ..models.day_night_mode import DayNightMode
from ..models.order_status import OrderStatus


class StoredStandardOrderRequestProperties(BaseModel):
    """Feature properties model for standard priority stored order

    Attributes:
        datetime (str): The closed date-time interval of the tasking order request.
        status (OrderStatus):
        created_at (datetime.datetime): The datetime at which the order was created.
        updated_at (datetime.datetime): The datetime at which the order was last updated.
        addon_withhold (Union[None, str]): Optional ISO8601 string describing the duration that an order will be
            withheld from the public catalog. Withhold options are specific to the contract. If not specified, the option
            will be set to the default specified in the relevant contract.
        name (Union[None, str]): The name of the order.
        product (Union[Literal['standard'], None]): Standard Priority. Default: 'standard'.
        satvu_day_night_mode (Union[None, DayNightMode]):
        max_cloud_cover (Union[None, int]): The max threshold of acceptable cloud coverage. Measured in percent.
            Default: 15.
        min_off_nadir (Union[None, int]): The minimum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Default: 0.
        max_off_nadir (Union[None, int]): The maximum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Must be larger than `min_off_nadir`. Default: 30.
    """

    datetime: str = Field(
        ..., description="The closed date-time interval of the tasking order request."
    )
    status: OrderStatus = Field(..., description=None)
    created_at: datetime.datetime = Field(
        ..., description="The datetime at which the order was created."
    )
    updated_at: datetime.datetime = Field(
        ..., description="The datetime at which the order was last updated."
    )
    addon_withhold: Union[None, str] = Field(
        None,
        description="Optional ISO8601 string describing the duration that an order will be withheld from the public catalog. Withhold options are specific to the contract. If not specified, the option will be set to the default specified in the relevant contract.",
    )
    name: Union[None, str] = Field(None, description="The name of the order.")
    product: Union[Literal["standard"], None] = Field(
        "standard", description="Standard Priority."
    )
    satvu_day_night_mode: Union[None, DayNightMode] = Field(None, description=None)
    max_cloud_cover: Union[None, int] = Field(
        15,
        description="The max threshold of acceptable cloud coverage. Measured in percent.",
    )
    min_off_nadir: Union[None, int] = Field(
        0,
        description="The minimum angle from the sensor between nadir and the scene center. Measured in decimal degrees.",
    )
    max_off_nadir: Union[None, int] = Field(
        30,
        description="The maximum angle from the sensor between nadir and the scene center. Measured in decimal degrees. Must be larger than `min_off_nadir`.",
    )
