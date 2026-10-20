# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Literal
from uuid import UUID

import pydantic

if TYPE_CHECKING:
    from ..models.point import Point
    from ..models.standard_feasibility_response_properties import (
        StandardFeasibilityResponseProperties,
    )


class StandardFeasibilityResponseFeature(pydantic.BaseModel):
    """Object representing a standard feasibility response.

    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (StandardFeasibilityResponseProperties): Properties of the standard priority feasibility response.
        id (UUID): The ID of the feasibility request.
    """

    type_: Literal["Feature"] = pydantic.Field(
        default="Feature", description=None, alias="type"
    )
    geometry: Point = pydantic.Field(
        ..., description="""Point Model""", alias="geometry"
    )
    properties: StandardFeasibilityResponseProperties = pydantic.Field(
        ...,
        description="""Properties of the standard priority feasibility response.""",
        alias="properties",
    )
    id: UUID = pydantic.Field(
        ..., description="""The ID of the feasibility request.""", alias="id"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
