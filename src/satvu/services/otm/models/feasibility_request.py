# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union

import pydantic

if TYPE_CHECKING:
    from ..models.assured_feasibility_fields import AssuredFeasibilityFields
    from ..models.point import Point
    from ..models.standard_request_properties import StandardRequestProperties


class FeasibilityRequest(pydantic.BaseModel):
    """Payload for feasibility request.

    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union['AssuredFeasibilityFields', 'StandardRequestProperties']): A map of additional metadata about
            the requested image.
    """

    type_: Literal["Feature"] = pydantic.Field(
        default="Feature", description=None, alias="type"
    )
    geometry: Point = pydantic.Field(
        ..., description="""Point Model""", alias="geometry"
    )
    properties: Union[AssuredFeasibilityFields, StandardRequestProperties] = (
        pydantic.Field(
            ...,
            description="""A map of additional metadata about the requested image.""",
            alias="properties",
        )
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
