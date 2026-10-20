# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Literal, Union

import pydantic

if TYPE_CHECKING:
    from ..models.assured_feasibility_fields_with_addons import (
        AssuredFeasibilityFieldsWithAddons,
    )
    from ..models.point import Point
    from ..models.price_information import PriceInformation
    from ..models.standard_order_fields_with_addons import StandardOrderFieldsWithAddons


class OrderPrice(pydantic.BaseModel):
    """
    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union['AssuredFeasibilityFieldsWithAddons', 'StandardOrderFieldsWithAddons']): A map of additional
            metadata about the requested image.
        created_at (datetime.datetime): The current UTC time.
        price (PriceInformation): Pricing information.
    """

    type_: Literal["Feature"] = pydantic.Field(
        default="Feature", description=None, alias="type"
    )
    geometry: Point = pydantic.Field(
        ..., description="""Point Model""", alias="geometry"
    )
    properties: Union[
        AssuredFeasibilityFieldsWithAddons, StandardOrderFieldsWithAddons
    ] = pydantic.Field(
        ...,
        description="""A map of additional metadata about the requested image.""",
        alias="properties",
    )
    created_at: datetime.datetime = pydantic.Field(
        ..., description="""The current UTC time.""", alias="created_at"
    )
    price: PriceInformation = pydantic.Field(
        ..., description="""Pricing information.""", alias="price"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
