# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Literal
from uuid import UUID

import pydantic

if TYPE_CHECKING:
    from ..models.point import Point
    from ..models.standard_order_request_properties import (
        StandardOrderRequestProperties,
    )


class ResellerStandardOrderRequest(pydantic.BaseModel):
    """Payload for reseller standard order request.

    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (StandardOrderRequestProperties):
        reseller_end_user_id (UUID):
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
    reseller_end_user_id: UUID = pydantic.Field(
        ..., description=None, alias="reseller_end_user_id"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
