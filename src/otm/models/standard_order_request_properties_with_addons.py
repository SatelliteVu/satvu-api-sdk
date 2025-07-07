from dataclasses import dataclass
from typing import Literal, Union

from ..models.day_night_mode import DayNightMode
from ..types import Unset


@dataclass
class StandardOrderRequestPropertiesWithAddons:
    """
    Attributes:
        datetime_ (str): The closed date-time interval of the tasking order request.
        addonwithhold (Union[None, str]): Optional ISO8601 string describing the duration that an order will be withheld
            from the public catalog. Withhold options are specific to the contract. If not specified, the option will be set
            to the default specified in the relevant contract.
        name (Union[None, str]): The name of the order.
        product (Union[Literal['standard'], Unset]): Standard Priority. Default: 'standard'.
        satvuday_night_mode (Union[None, DayNightMode]):
        max_cloud_cover (Union[None, int]): The max threshold of acceptable cloud coverage. Measured in percent.
            Default: 15.
        min_off_nadir (Union[None, int]): The minimum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Default: 0.
        max_off_nadir (Union[None, int]): The maximum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Must be larger than `min_off_nadir`. Default: 30.
    """

    datetime_: str
    addonwithhold: Union[None, str] = None
    name: Union[None, str] = None
    product: Union[Literal["standard"], Unset] = "standard"
    satvuday_night_mode: Union[None, DayNightMode] = None
    max_cloud_cover: Union[None, int] = 15
    min_off_nadir: Union[None, int] = 0
    max_off_nadir: Union[None, int] = 30

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "datetime",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "datetime": str,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "addon:withhold": object,
            "name": object,
            "product": object,
            "satvu:day_night_mode": object,
            "max_cloud_cover": int,
            "min_off_nadir": int,
            "max_off_nadir": int,
        }
