import datetime
from typing import Literal, Union

from pydantic import BaseModel

from ..models.day_night_mode import DayNightMode
from ..models.order_status import OrderStatus


class SearchStandardOrderProperties(BaseModel):
    """Search response properties for standard orders

    Attributes:
        datetime (str): The closed date-time interval of the tasking order request.
        status (OrderStatus):
        created_at (datetime.datetime): The datetime at which the order was created.
        updated_at (datetime.datetime): The datetime at which the order was last updated.
        stac_item_id (Union[None, str]): The item id of the STAC item that fulfilled the order, if the order has been
            fulfilled.
        stac_datetime (Union[None, datetime.datetime]): The acquisition datetime of the STAC item that fulfilled the
            order, if the order has been fulfilled.
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

    datetime: str
    status: OrderStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
    stac_item_id: Union[None, str] = None
    stac_datetime: Union[None, datetime.datetime] = None
    addon_withhold: Union[None, str] = None
    name: Union[None, str] = None
    product: Union[Literal["standard"], None] = "standard"
    satvu_day_night_mode: Union[None, DayNightMode] = None
    max_cloud_cover: Union[None, int] = 15
    min_off_nadir: Union[None, int] = 0
    max_off_nadir: Union[None, int] = 30
