from typing import Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from ..models.notification_description import NotificationDescription
from ..models.reseller_notification_description import ResellerNotificationDescription


class PostWebhookResponse(BaseModel):
    """
    Attributes:
        active (bool): Whether the webhook is active.
        event_types (list[Union[NotificationDescription, ResellerNotificationDescription]]): List of events that the
            webhook is subscribed to.
        name (str): The name of the webhook.
        url (str): The URL where events are received.
        id (UUID): A unique identifier for the webhook.
        signing_key (str): The webhook signing key for payload decryption.
    """

    active: bool = Field(
        ..., description="Whether the webhook is active.", alias="active"
    )
    event_types: list[
        Union[NotificationDescription, ResellerNotificationDescription]
    ] = Field(
        ...,
        description="List of events that the webhook is subscribed to.",
        alias="event_types",
    )
    name: str = Field(..., description="The name of the webhook.", alias="name")
    url: str = Field(..., description="The URL where events are received.", alias="url")
    id: UUID = Field(
        ..., description="A unique identifier for the webhook.", alias="id"
    )
    signing_key: str = Field(
        ...,
        description="The webhook signing key for payload decryption.",
        alias="signing_key",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
