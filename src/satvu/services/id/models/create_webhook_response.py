# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from uuid import UUID

import pydantic

if TYPE_CHECKING:
    from ..models.notification_description import NotificationDescription


class CreateWebhookResponse(pydantic.BaseModel):
    """
    Attributes:
        active (bool): Whether the webhook is active.
        event_types (list[NotificationDescription]): List of events that the webhook is subscribed to.
        name (str): The name of the webhook.
        url (str): The URL where events are received.
        id (UUID): A unique identifier for the webhook.
        signing_key (str): The signing key used to verify webhook payload signatures.
        unreachable_warning (Union[None, str]): An optional warning if the URL is not reachable.
    """

    active: bool = pydantic.Field(
        ..., description="""Whether the webhook is active.""", alias="active"
    )
    event_types: list[NotificationDescription] = pydantic.Field(
        ...,
        description="""List of events that the webhook is subscribed to.""",
        alias="event_types",
    )
    name: str = pydantic.Field(
        ..., description="""The name of the webhook.""", alias="name"
    )
    url: str = pydantic.Field(
        ..., description="""The URL where events are received.""", alias="url"
    )
    id: UUID = pydantic.Field(
        ..., description="""A unique identifier for the webhook.""", alias="id"
    )
    signing_key: str = pydantic.Field(
        ...,
        description="""The signing key used to verify webhook payload signatures.""",
        alias="signing_key",
    )
    unreachable_warning: Union[None, str] = pydantic.Field(
        default=None,
        description="""An optional warning if the URL is not reachable.""",
        alias="unreachable_warning",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
