from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Literal, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.price import Price


class AssuredFeasibilityResponseProperties(BaseModel):
    """Properties of the assured priority feasibility response.

    Attributes:
        product (Literal['assured']): Assured Priority.
        datetime_ (str): The closed date-time interval of the response.
        created_at (datetime.datetime): The datetime at which the feasibility response was created.
        updated_at (datetime.datetime): The datetime at which the feasibility response was last updated.
        price (Union['Price', None]): Pricing information.
        min_sun_el (float | None): The minimum sun elevation angle of the pass. Measured in decimal degrees from the
            horizontal.
        max_sun_el (float | None): The maximum sun elevation angle of the pass. Measured in decimal degrees from the
            horizontal.
        min_gsd (float | None): The minimum ground sample distance value of the pass. Measured in metres representing
            the square root of the area of the pixel size projected onto the earth.
        max_gsd (float | None): The maximum ground sample distance value of the pass. Measured in metres representing
            the square root of the area of the pixel size projected onto the earth.
        min_off_nadir (float | None): The minimum angle from the sensor between nadir and the scene center. Measured in
            decimal degrees.
        max_off_nadir (float | None): The maximum angle from the sensor between nadir and the scene center. Measured in
            decimal degrees.
    """

    product: Literal["assured"] = Field(
        "assured", description="Assured Priority.", alias="product"
    )
    datetime_: str = Field(
        ...,
        description="The closed date-time interval of the response.",
        alias="datetime",
    )
    created_at: datetime.datetime = Field(
        ...,
        description="The datetime at which the feasibility response was created.",
        alias="created_at",
    )
    updated_at: datetime.datetime = Field(
        ...,
        description="The datetime at which the feasibility response was last updated.",
        alias="updated_at",
    )
    price: Union["Price", None] = Field(
        None, description="Pricing information.", alias="price"
    )
    min_sun_el: float | None = Field(
        None,
        description="The minimum sun elevation angle of the pass. Measured in decimal degrees from the horizontal.",
        alias="min_sun_el",
    )
    max_sun_el: float | None = Field(
        None,
        description="The maximum sun elevation angle of the pass. Measured in decimal degrees from the horizontal.",
        alias="max_sun_el",
    )
    min_gsd: float | None = Field(
        None,
        description="The minimum ground sample distance value of the pass. Measured in metres representing the square root of the area of the pixel size projected onto the earth.",
        alias="min_gsd",
    )
    max_gsd: float | None = Field(
        None,
        description="The maximum ground sample distance value of the pass. Measured in metres representing the square root of the area of the pixel size projected onto the earth.",
        alias="max_gsd",
    )
    min_off_nadir: float | None = Field(
        None,
        description="The minimum angle from the sensor between nadir and the scene center. Measured in decimal degrees.",
        alias="min_off_nadir",
    )
    max_off_nadir: float | None = Field(
        None,
        description="The maximum angle from the sensor between nadir and the scene center. Measured in decimal degrees.",
        alias="max_off_nadir",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
