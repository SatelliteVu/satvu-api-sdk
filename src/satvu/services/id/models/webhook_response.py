# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.notification_description import NotificationDescription


class WebhookResponse(BaseModel):
    """
    Attributes:
        active (bool): Whether the webhook is active.
        event_types (list[NotificationDescription]): List of events that the webhook is subscribed to.
        name (str): The name of the webhook.
        url (str): The URL where events are received.
        id (UUID): A unique identifier for the webhook.
    """

    active: bool = Field(
        ..., description="""Whether the webhook is active.""", alias="active"
    )
    event_types: list[NotificationDescription] = Field(
        ...,
        description="""List of events that the webhook is subscribed to.""",
        alias="event_types",
    )
    name: str = Field(..., description="""The name of the webhook.""", alias="name")
    url: str = Field(
        ..., description="""The URL where events are received.""", alias="url"
    )
    id: UUID = Field(
        ..., description="""A unique identifier for the webhook.""", alias="id"
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
