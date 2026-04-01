# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.reseller_webhook_event import ResellerWebhookEvent
from ..models.webhook_event import WebhookEvent


class EditWebhookPayload(BaseModel):
    """
    Attributes:
        active (Union[None, bool]): Whether the webhook should be active or not.
        event_types (Union[None, list[Union['ResellerWebhookEvent', 'WebhookEvent']]]): A list of events to subscribe
            to.
        name (Union[None, str]): The name of the webhook.
    """

    active: Union[None, bool] = Field(
        default=None,
        description="""Whether the webhook should be active or not.""",
        alias="active",
    )
    event_types: Union[None, list[Union[ResellerWebhookEvent, WebhookEvent]]] = Field(
        default=None,
        description="""A list of events to subscribe to.""",
        alias="event_types",
    )
    name: Union[None, str] = Field(
        default=None, description="""The name of the webhook.""", alias="name"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
