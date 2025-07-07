import datetime
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, Union

from ..models.day_night_mode import DayNightMode
from ..types import Unset

if TYPE_CHECKING:
    from ..models.price import Price


@dataclass
class StandardFeasibilityResponseProperties:
    """Properties of the standard priority feasibility response.

    Attributes:
        datetime_ (str): The closed date-time interval of the tasking order request.
        created_at (datetime.datetime): The datetime at which the feasibility response was created.
        updated_at (datetime.datetime): The datetime at which the feasibility response was last updated.
        min_sun_el (float): The minimum sun elevation angle of the pass. Measured in decimal degrees from the
            horizontal.
        max_sun_el (float): The maximum sun elevation angle of the pass. Measured in decimal degrees from the
            horizontal.
        min_gsd (float): The minimum ground sample distance value of the pass. Measured in metres representing the
            square root of the area of the pixel size projected onto the earth.
        max_gsd (float): The maximum ground sample distance value of the pass. Measured in metres representing the
            square root of the area of the pixel size projected onto the earth.
        name (Union[None, str]): The name of the order.
        product (Union[Literal['standard'], Unset]): Standard Priority. Default: 'standard'.
        satvuday_night_mode (Union[None, DayNightMode]):
        max_cloud_cover (Union[None, int]): The max threshold of acceptable cloud coverage. Measured in percent.
            Default: 15.
        min_off_nadir (Union[None, int]): The minimum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Default: 0.
        max_off_nadir (Union[None, int]): The maximum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Must be larger than `min_off_nadir`. Default: 30.
        price (Union['Price', None]): Pricing information.
    """

    datetime_: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    min_sun_el: float
    max_sun_el: float
    min_gsd: float
    max_gsd: float
    name: Union[None, str] = None
    product: Union[Literal["standard"], Unset] = "standard"
    satvuday_night_mode: Union[None, DayNightMode] = None
    max_cloud_cover: Union[None, int] = 15
    min_off_nadir: Union[None, int] = 0
    max_off_nadir: Union[None, int] = 30
    price: Union["Price", None] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "datetime",
            "created_at",
            "updated_at",
            "min_sun_el",
            "max_sun_el",
            "min_gsd",
            "max_gsd",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "datetime": str,
            "created_at": object,
            "updated_at": object,
            "min_sun_el": float,
            "max_sun_el": float,
            "min_gsd": float,
            "max_gsd": float,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "name": object,
            "product": object,
            "satvu:day_night_mode": object,
            "max_cloud_cover": int,
            "min_off_nadir": int,
            "max_off_nadir": int,
            "price": object,
        }
