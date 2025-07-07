import datetime
from typing import Literal, Union

from pydantic import BaseModel

from ..models.price import Price


class ExtraIgnoreAssuredFeasibilityResponseProperties(BaseModel):
    """
    Attributes:
        product (Literal['assured']): Assured Priority.
        datetime (str): The closed date-time interval of the request.
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
        price (Union[None, Price]): Pricing information.
    """

    product: Literal["assured"]
    datetime: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    min_sun_el: float
    max_sun_el: float
    min_gsd: float
    max_gsd: float
    min_off_nadir: float
    max_off_nadir: float
    price: Union[None, Price] = None
