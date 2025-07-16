from typing import Union
from uuid import UUID

from pydantic import BaseModel, Field

from ..models.notification_description import NotificationDescription
from ..models.reseller_notification_description import ResellerNotificationDescription


class CreateWebhookResponse(BaseModel):
    """
    Attributes:
        active (bool): Whether the webhook is active.
        event_types (list[Union[NotificationDescription, ResellerNotificationDescription]]): List of events that the
            webhook is subscribed to.
        name (str): The name of the webhook.
        url (str): The URL where events are received.
        id (UUID): A unique identifier for the webhook.
        signing_key (str): The webhook signing key for payload decryption.
        unreachable_warning (Union[None, str]): An optional warning if the URL is not reachable.
    """

    active: bool = Field(..., description="Whether the webhook is active.")
    event_types: list[
        Union[NotificationDescription, ResellerNotificationDescription]
    ] = Field(..., description="List of events that the webhook is subscribed to.")
    name: str = Field(..., description="The name of the webhook.")
    url: str = Field(..., description="The URL where events are received.")
    id: UUID = Field(..., description="A unique identifier for the webhook.")
    signing_key: str = Field(
        ..., description="The webhook signing key for payload decryption."
    )
    unreachable_warning: Union[None, str] = Field(
        None, description="An optional warning if the URL is not reachable."
    )
