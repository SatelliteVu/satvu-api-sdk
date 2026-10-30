# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, Literal, Union

import pydantic

from satvu.shared.discriminators import const_tag

if TYPE_CHECKING:
    from ..models.assured_feasibility_fields_with_addons import (
        AssuredFeasibilityFieldsWithAddons,
    )
    from ..models.point import Point
    from ..models.standard_price_request_properties import (
        StandardPriceRequestProperties,
    )


class PriceRequest(pydantic.BaseModel):
    """Payload for price request.

    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union['AssuredFeasibilityFieldsWithAddons', 'StandardPriceRequestProperties']): A map of additional
            metadata about the requested image.
    """

    type_: Literal["Feature"] = pydantic.Field(
        default="Feature", description=None, alias="type"
    )
    geometry: Point = pydantic.Field(
        ..., description="""Point Model""", alias="geometry"
    )
    properties: Annotated[
        Union[
            Annotated[AssuredFeasibilityFieldsWithAddons, pydantic.Tag("assured")],
            Annotated[StandardPriceRequestProperties, pydantic.Tag("standard")],
        ],
        pydantic.Discriminator(const_tag("product", default="standard")),
    ] = pydantic.Field(
        ...,
        description="""A map of additional metadata about the requested image.""",
        alias="properties",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
