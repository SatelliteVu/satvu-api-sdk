from typing import Literal, Union

from pydantic import BaseModel, Field

from ..models.day_night_mode import DayNightMode
from ..models.feasibility_request_status import FeasibilityRequestStatus
from ..models.price import Price


class StandardStoredFeasibilityRequestProperties(BaseModel):
    """Properties of the stored standard priority feasibility request.

    Attributes:
        datetime (str): The closed date-time interval of the tasking order request.
        status (FeasibilityRequestStatus):
        created_at (datetime.datetime): The datetime at which the feasibility request was created.
        updated_at (datetime.datetime): The datetime at which the feasibility request was last updated.
        product (Union[Literal['standard'], None]): Standard Priority. Default: 'standard'.
        satvu_day_night_mode (Union[None, DayNightMode]):
        max_cloud_cover (Union[None, int]): The max threshold of acceptable cloud coverage. Measured in percent.
            Default: 15.
        min_off_nadir (Union[None, int]): The minimum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Default: 0.
        max_off_nadir (Union[None, int]): The maximum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Must be larger than `min_off_nadir`. Default: 30.
        price (Union[None, Price]): Pricing information.
    """

    datetime: str = Field(
        ..., description="The closed date-time interval of the tasking order request."
    )
    status: FeasibilityRequestStatus = Field(..., description=None)
    created_at: datetime.datetime = Field(
        ..., description="The datetime at which the feasibility request was created."
    )
    updated_at: datetime.datetime = Field(
        ...,
        description="The datetime at which the feasibility request was last updated.",
    )
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
    price: Union[None, Price] = Field(None, description="Pricing information.")
