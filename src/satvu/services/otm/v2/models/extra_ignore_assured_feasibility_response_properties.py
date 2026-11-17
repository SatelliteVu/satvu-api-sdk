# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Any, Literal, Union

import pydantic

if TYPE_CHECKING:
    from ..models.price import Price


class ExtraIgnoreAssuredFeasibilityResponseProperties(pydantic.BaseModel):
    """
    Attributes:
        product (Literal['assured']): The tasking product. Always `assured` (Assured tasking).
        datetime_ (str): The acquisition window of the pass, as an ISO 8601 interval (`start/end`).
        created_at (datetime.datetime): When the feasibility response was created.
        updated_at (datetime.datetime): When the feasibility response was last updated.
        price (Union['Price', None]): Pricing information.
        min_sun_el (float | None): The minimum sun elevation angle. For Assured tasking, the estimate for the pass; for
            Standard tasking, the lowest that `satvu:day_night_mode` allows. Measured in decimal degrees from the
            horizontal.
        max_sun_el (float | None): The maximum sun elevation angle. For Assured tasking, the estimate for the pass; for
            Standard tasking, the highest that `satvu:day_night_mode` allows. Measured in decimal degrees from the
            horizontal.
        min_gsd (float | None): The minimum ground sample distance. For Assured tasking, the estimate for the pass; for
            Standard tasking, the lowest that may be delivered. Measured in meters, as the square root of the pixel area
            projected onto Earth.
        max_gsd (float | None): The maximum ground sample distance. For Assured tasking, the estimate for the pass; for
            Standard tasking, the highest that may be delivered. Measured in meters, as the square root of the pixel area
            projected onto Earth.
        min_off_nadir (float | None): The minimum angle from the sensor between nadir and the scene center. Measured in
            decimal degrees.
        max_off_nadir (float | None): The maximum angle from the sensor between nadir and the scene center. Measured in
            decimal degrees.
    """

    product: Literal["assured"] = pydantic.Field(
        default="assured",
        description="""The tasking product. Always `assured` (Assured tasking).""",
        alias="product",
    )
    datetime_: str = pydantic.Field(
        ...,
        description="""The acquisition window of the pass, as an ISO 8601 interval (`start/end`).""",
        alias="datetime",
    )
    created_at: datetime.datetime = pydantic.Field(
        ...,
        description="""When the feasibility response was created.""",
        alias="created_at",
    )
    updated_at: datetime.datetime = pydantic.Field(
        ...,
        description="""When the feasibility response was last updated.""",
        alias="updated_at",
    )
    price: Union[Price, None] = pydantic.Field(
        default=None, description="""Pricing information.""", alias="price"
    )
    min_sun_el: float | None = pydantic.Field(
        default=None,
        description="""The minimum sun elevation angle. For Assured tasking, the estimate for the pass; for Standard tasking, the lowest that `satvu:day_night_mode` allows. Measured in decimal degrees from the horizontal.""",
        alias="min_sun_el",
    )
    max_sun_el: float | None = pydantic.Field(
        default=None,
        description="""The maximum sun elevation angle. For Assured tasking, the estimate for the pass; for Standard tasking, the highest that `satvu:day_night_mode` allows. Measured in decimal degrees from the horizontal.""",
        alias="max_sun_el",
    )
    min_gsd: float | None = pydantic.Field(
        default=None,
        description="""The minimum ground sample distance. For Assured tasking, the estimate for the pass; for Standard tasking, the lowest that may be delivered. Measured in meters, as the square root of the pixel area projected onto Earth.""",
        alias="min_gsd",
    )
    max_gsd: float | None = pydantic.Field(
        default=None,
        description="""The maximum ground sample distance. For Assured tasking, the estimate for the pass; for Standard tasking, the highest that may be delivered. Measured in meters, as the square root of the pixel area projected onto Earth.""",
        alias="max_gsd",
    )
    min_off_nadir: float | None = pydantic.Field(
        default=None,
        description="""The minimum angle from the sensor between nadir and the scene center. Measured in decimal degrees.""",
        alias="min_off_nadir",
    )
    max_off_nadir: float | None = pydantic.Field(
        default=None,
        description="""The maximum angle from the sensor between nadir and the scene center. Measured in decimal degrees.""",
        alias="max_off_nadir",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )

    def model_post_init(self, context: Any, /) -> None:
        # Required fields the SDK fills in (constants, spec defaults) must survive
        # model_dump(exclude_unset=True)
        self.__pydantic_fields_set__ = self.model_fields_set.union(["product"])
