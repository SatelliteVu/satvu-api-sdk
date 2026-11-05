# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal
from uuid import UUID

import pydantic

if TYPE_CHECKING:
    from ..models.assured_feasibility_response_properties import (
        AssuredFeasibilityResponseProperties,
    )
    from ..models.point import Point


class AssuredFeasibilityResponseFeature(pydantic.BaseModel):
    """Object representing an assured feasibility response.

    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (AssuredFeasibilityResponseProperties): Properties of the assured priority feasibility response.
        id (UUID): The ID of the feasibility request.
        signature (str): Signature token.
    """

    type_: Literal["Feature"] = pydantic.Field(
        default="Feature", description=None, alias="type"
    )
    geometry: Point = pydantic.Field(
        ..., description="""Point Model""", alias="geometry"
    )
    properties: AssuredFeasibilityResponseProperties = pydantic.Field(
        ...,
        description="""Properties of the assured priority feasibility response.""",
        alias="properties",
    )
    id: UUID = pydantic.Field(
        ..., description="""The ID of the feasibility request.""", alias="id"
    )
    signature: str = pydantic.Field(
        ..., description="""Signature token.""", alias="signature"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )

    def model_post_init(self, context: Any, /) -> None:
        # Required fields the SDK fills in (constants, spec defaults) must survive
        # model_dump(exclude_unset=True)
        self.__pydantic_fields_set__ = self.model_fields_set.union(["type_"])
