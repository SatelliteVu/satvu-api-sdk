# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.tasking_order_fulfilled_payload_v2 import (
        TaskingOrderFulfilledPayloadV2,
    )


class TaskingOrderFulfilledWebhookV2(BaseModel):
    """Envelope delivered when a tasking order is fulfilled (schema v2).

    Attributes:
        type_ (str): Event topic identifier
        timestamp (int): UTC Unix timestamp (seconds) at which the event was emitted
        data (TaskingOrderFulfilledPayloadV2):
    """

    type_: str = Field(..., description="""Event topic identifier""", alias="type")
    timestamp: int = Field(
        ...,
        description="""UTC Unix timestamp (seconds) at which the event was emitted""",
        alias="timestamp",
    )
    data: TaskingOrderFulfilledPayloadV2 = Field(..., description=None, alias="data")

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
