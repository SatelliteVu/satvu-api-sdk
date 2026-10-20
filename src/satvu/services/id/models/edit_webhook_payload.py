# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

import pydantic

from ..models.reseller_webhook_event import ResellerWebhookEvent
from ..models.webhook_event import WebhookEvent


class EditWebhookPayload(pydantic.BaseModel):
    """
    Attributes:
        active (Union[None, bool]): Whether the webhook should be active or not.
        event_types (Union[None, list[Union['ResellerWebhookEvent', 'WebhookEvent']]]): A list of events to subscribe
            to.
        name (Union[None, str]): The name of the webhook.
    """

    active: Union[None, bool] = pydantic.Field(
        default=None,
        description="""Whether the webhook should be active or not.""",
        alias="active",
    )
    event_types: Union[None, list[Union[ResellerWebhookEvent, WebhookEvent]]] = (
        pydantic.Field(
            default=None,
            description="""A list of events to subscribe to.""",
            alias="event_types",
        )
    )
    name: Union[None, str] = pydantic.Field(
        default=None, description="""The name of the webhook.""", alias="name"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
