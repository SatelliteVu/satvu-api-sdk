from typing import Literal

from pydantic import BaseModel, Field


class NotificationDescription(BaseModel):
    """
    Attributes:
        topic (Literal['tasking:order_status']): Notification topic.
        name (str): Name of notification type.
        description (str): Description of notification type.
    """

    topic: Literal["tasking:order_status"] = Field(
        "tasking:order_status", description="Notification topic."
    )
    name: str = Field(..., description="Name of notification type.")
    description: str = Field(..., description="Description of notification type.")
