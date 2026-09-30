# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.end_user_kyc_status_update_payload import (
        EndUserKYCStatusUpdatePayload,
    )


class EndUserKYCStatusUpdateWebhook(BaseModel):
    """Envelope delivered when an end user's KYC status changes.

    Attributes:
        type_ (str): Event topic identifier
        timestamp (int): UTC Unix timestamp (seconds) at which the event was emitted
        data (EndUserKYCStatusUpdatePayload):
    """

    type_: str = Field(..., description="""Event topic identifier""", alias="type")
    timestamp: int = Field(
        ...,
        description="""UTC Unix timestamp (seconds) at which the event was emitted""",
        alias="timestamp",
    )
    data: EndUserKYCStatusUpdatePayload = Field(..., description=None, alias="data")

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
