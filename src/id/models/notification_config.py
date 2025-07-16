from typing import Literal, Union

from pydantic import BaseModel, Field


class NotificationConfig(BaseModel):
    """
    Attributes:
        topic (Literal['tasking:order_status']): Notification topic.
        email (Union[None, bool]): Opted into email notifications. Default: False.
    """

    topic: Literal["tasking:order_status"] = Field(
        "tasking:order_status", description="Notification topic."
    )
    email: Union[None, bool] = Field(
        False, description="Opted into email notifications."
    )
