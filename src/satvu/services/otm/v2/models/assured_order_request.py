# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

import pydantic

if TYPE_CHECKING:
    from ..models.assured_order_request_properties import AssuredOrderRequestProperties


class AssuredOrderRequest(pydantic.BaseModel):
    """
    Attributes:
        properties (AssuredOrderRequestProperties):
    """

    properties: AssuredOrderRequestProperties = pydantic.Field(
        ..., description=None, alias="properties"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
