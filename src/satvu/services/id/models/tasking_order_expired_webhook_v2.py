# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

import pydantic

if TYPE_CHECKING:
    from ..models.tasking_order_expired_payload_v2 import TaskingOrderExpiredPayloadV2


class TaskingOrderExpiredWebhookV2(pydantic.BaseModel):
    """Envelope delivered when a tasking order expires (schema v2).

    Attributes:
        type_ (str): Event topic identifier
        timestamp (int): UTC Unix timestamp (seconds) at which the event was emitted
        data (TaskingOrderExpiredPayloadV2):
    """

    type_: str = pydantic.Field(
        ..., description="""Event topic identifier""", alias="type"
    )
    timestamp: int = pydantic.Field(
        ...,
        description="""UTC Unix timestamp (seconds) at which the event was emitted""",
        alias="timestamp",
    )
    data: TaskingOrderExpiredPayloadV2 = pydantic.Field(
        ..., description=None, alias="data"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
