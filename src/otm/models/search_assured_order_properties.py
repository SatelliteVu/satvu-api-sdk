import datetime
from typing import Literal, Union

from pydantic import BaseModel

from ..models.day_night_mode import DayNightMode
from ..models.order_status import OrderStatus


class SearchAssuredOrderProperties(BaseModel):
    """Search response properties for assured orders

    Attributes:
        product (Literal['assured']): Assured Priority.
        datetime (str): The closed date-time interval of the tasking order request.
        signature (str): Signature token.
        status (OrderStatus):
        created_at (datetime.datetime): The datetime at which the order was created.
        updated_at (datetime.datetime): The datetime at which the order was last updated.
        stac_item_id (Union[None, str]): The item id of the STAC item that fulfilled the order, if the order has been
            fulfilled.
        stac_datetime (Union[None, datetime.datetime]): The acquisition datetime of the STAC item that fulfilled the
            order, if the order has been fulfilled.
        name (Union[None, str]): The name of the order.
        satvu_day_night_mode (Union[None, DayNightMode]):
        max_cloud_cover (Union[None, int]): The max threshold of acceptable cloud coverage. Measured in percent.
            Default: 15.
        min_off_nadir (Union[None, int]): The minimum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Default: 0.
        max_off_nadir (Union[None, int]): The maximum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Must be larger than `min_off_nadir`. Default: 30.
        addon_withhold (Union[None, str]): Optional ISO8601 string describing the duration that an order will be
            withheld from the public catalog. Withhold options are specific to the contract. If not specified, the option
            will be set to the default specified in the relevant contract.
    """

    product: Literal["assured"]
    datetime: str
    signature: str
    status: OrderStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
    stac_item_id: Union[None, str] = None
    stac_datetime: Union[None, datetime.datetime] = None
    name: Union[None, str] = None
    satvu_day_night_mode: Union[None, DayNightMode] = None
    max_cloud_cover: Union[None, int] = 15
    min_off_nadir: Union[None, int] = 0
    max_off_nadir: Union[None, int] = 30
    addon_withhold: Union[None, str] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "product",
            "datetime",
            "signature",
            "status",
            "created_at",
            "updated_at",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "product": object,
            "datetime": str,
            "signature": str,
            "status": object,
            "created_at": object,
            "updated_at": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "stac:item_id": object,
            "stac:datetime": object,
            "name": object,
            "satvu:day_night_mode": object,
            "max_cloud_cover": int,
            "min_off_nadir": int,
            "max_off_nadir": int,
            "addon:withhold": object,
        }
