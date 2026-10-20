# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

import pydantic

from ..models.reseller_webhook_event import ResellerWebhookEvent
from ..models.webhook_event import WebhookEvent


class CoreWebhook(pydantic.BaseModel):
    """
    Attributes:
        event_types (list[Union['ResellerWebhookEvent', 'WebhookEvent']]): A list of events to subscribe to.
        name (str): The name of the webhook.
        url (str): The URL where you want to receive requests for events you are subscribed to. Must be HTTPS.
    """

    event_types: list[Union[ResellerWebhookEvent, WebhookEvent]] = pydantic.Field(
        ..., description="""A list of events to subscribe to.""", alias="event_types"
    )
    name: str = pydantic.Field(
        ..., description="""The name of the webhook.""", alias="name"
    )
    url: str = pydantic.Field(
        ...,
        description="""The URL where you want to receive requests for events you are subscribed to. Must be HTTPS.""",
        alias="url",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
