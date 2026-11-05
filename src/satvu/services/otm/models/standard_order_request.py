# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

import pydantic

if TYPE_CHECKING:
    from ..models.point import Point
    from ..models.standard_order_request_properties import (
        StandardOrderRequestProperties,
    )


class StandardOrderRequest(pydantic.BaseModel):
    """Payload for standard order request.

    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (StandardOrderRequestProperties):
    """

    type_: Literal["Feature"] = pydantic.Field(
        default="Feature", description=None, alias="type"
    )
    geometry: Point = pydantic.Field(
        ..., description="""Point Model""", alias="geometry"
    )
    properties: StandardOrderRequestProperties = pydantic.Field(
        ..., description=None, alias="properties"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )

    def model_post_init(self, context: Any, /) -> None:
        # Required fields the SDK fills in (constants, spec defaults) must survive
        # model_dump(exclude_unset=True)
        self.__pydantic_fields_set__ = self.model_fields_set.union(["type_"])
