# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pydantic

if TYPE_CHECKING:
    from ..models.assured_order_request_properties import AssuredOrderRequestProperties


class ResellerAssuredOrderRequest(pydantic.BaseModel):
    """Payload for reseller assured order request.

    Attributes:
        properties (AssuredOrderRequestProperties):
        reseller_end_user_id (UUID):
    """

    properties: AssuredOrderRequestProperties = pydantic.Field(
        ..., description=None, alias="properties"
    )
    reseller_end_user_id: UUID = pydantic.Field(
        ..., description=None, alias="reseller_end_user_id"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
