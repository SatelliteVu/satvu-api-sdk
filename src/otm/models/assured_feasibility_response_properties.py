from typing import Literal, Union

from pydantic import BaseModel, Field

from ..models.price import Price


class AssuredFeasibilityResponseProperties(BaseModel):
    """Properties of the assured priority feasibility response.

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

    product: Literal["assured"] = Field("assured", description="Assured Priority.")
    datetime: str = Field(
        ..., description="The closed date-time interval of the request."
    )
    created_at: datetime.datetime = Field(
        ..., description="The datetime at which the feasibility response was created."
    )
    updated_at: datetime.datetime = Field(
        ...,
        description="The datetime at which the feasibility response was last updated.",
    )
    min_sun_el: float = Field(
        ...,
        description="The minimum sun elevation angle of the pass. Measured in decimal degrees from the horizontal.",
    )
    max_sun_el: float = Field(
        ...,
        description="The maximum sun elevation angle of the pass. Measured in decimal degrees from the horizontal.",
    )
    min_gsd: float = Field(
        ...,
        description="The minimum ground sample distance value of the pass. Measured in metres representing the square root of the area of the pixel size projected onto the earth.",
    )
    max_gsd: float = Field(
        ...,
        description="The maximum ground sample distance value of the pass. Measured in metres representing the square root of the area of the pixel size projected onto the earth.",
    )
    min_off_nadir: float = Field(
        ...,
        description="The minimum angle from the sensor between nadir and the scene center. Measured in decimal degrees.",
    )
    max_off_nadir: float = Field(
        ...,
        description="The maximum angle from the sensor between nadir and the scene center. Measured in decimal degrees.",
    )
    price: Union[None, Price] = Field(None, description="Pricing information.")
