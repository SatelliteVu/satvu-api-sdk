import datetime
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, Union

if TYPE_CHECKING:
    from ..models.price import Price


@dataclass
class AssuredFeasibilityResponseProperties:
    """Properties of the assured priority feasibility response.

    Attributes:
        product (Literal['assured']): Assured Priority.
        datetime_ (str): The closed date-time interval of the request.
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
        min_off_nadir (float): The minimum angle from the sensor between nadir and the scene center. Measured in decimal
            degrees.
        max_off_nadir (float): The maximum angle from the sensor between nadir and the scene center. Measured in decimal
            degrees.
        price (Union['Price', None]): Pricing information.
    """

    product: Literal["assured"]
    datetime_: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    min_sun_el: float
    max_sun_el: float
    min_gsd: float
    max_gsd: float
    min_off_nadir: float
    max_off_nadir: float
    price: Union["Price", None] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "product",
            "datetime",
            "created_at",
            "updated_at",
            "min_sun_el",
            "max_sun_el",
            "min_gsd",
            "max_gsd",
            "min_off_nadir",
            "max_off_nadir",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "product": object,
            "datetime": str,
            "created_at": object,
            "updated_at": object,
            "min_sun_el": float,
            "max_sun_el": float,
            "min_gsd": float,
            "max_gsd": float,
            "min_off_nadir": float,
            "max_off_nadir": float,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "price": object,
        }
