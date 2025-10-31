from __future__ import annotations

import datetime
from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.day_night_mode import DayNightMode
from ..models.order_status import OrderStatus


class SearchStandardOrderProperties(BaseModel):
    """Search response properties for standard orders

    Attributes:
        datetime_ (str): The closed date-time interval of the tasking order request.
        status ('OrderStatus'):
        created_at (datetime.datetime): The datetime at which the order was created.
        updated_at (datetime.datetime): The datetime at which the order was last updated.
        stac_item_id (None | str): The item id of the STAC item that fulfilled the order, if the order has been
            fulfilled.
        stac_datetime (datetime.datetime | None): The acquisition datetime of the STAC item that fulfilled the order, if
            the order has been fulfilled.
        licence_level (None | str): The optional licence level for the order Licence levels are specific to the
            contract. If not specified, the option will be set to the licence with the smallest uplift in the relevant
            contract.
        addon_withhold (None | str): The optional ISO8601 string describing the duration that an order will be withheld
            from the public catalog. Withhold options are specific to the contract. If not specified, the option will be set
            to the default specified in the relevant contract.
        name (None | str): The name of the order.
        product (Union[Literal['standard'], None]): Standard Priority. Default: 'standard'.
        satvu_day_night_mode (Union[None, 'DayNightMode']):
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
    status: "OrderStatus" = Field(..., description=None, alias="status")
    created_at: datetime.datetime = Field(
        ...,
        description="The datetime at which the order was created.",
        alias="created_at",
    )
    updated_at: datetime.datetime = Field(
        ...,
        description="The datetime at which the order was last updated.",
        alias="updated_at",
    )
    stac_item_id: None | str = Field(
        None,
        description="The item id of the STAC item that fulfilled the order, if the order has been fulfilled.",
        alias="stac:item_id",
    )
    stac_datetime: datetime.datetime | None = Field(
        None,
        description="The acquisition datetime of the STAC item that fulfilled the order, if the order has been fulfilled.",
        alias="stac:datetime",
    )
    licence_level: None | str = Field(
        None,
        description="The optional licence level for the order Licence levels are specific to the contract. If not specified, the option will be set to the licence with the smallest uplift in the relevant contract.",
        alias="licence_level",
    )
    addon_withhold: None | str = Field(
        None,
        description="The optional ISO8601 string describing the duration that an order will be withheld from the public catalog. Withhold options are specific to the contract. If not specified, the option will be set to the default specified in the relevant contract.",
        alias="addon:withhold",
    )
    name: None | str = Field(None, description="The name of the order.", alias="name")
    product: Union[Literal["standard"], None] = Field(
        "standard", description="Standard Priority.", alias="product"
    )
    satvu_day_night_mode: Union[None, "DayNightMode"] = Field(
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
