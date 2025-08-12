from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field


class NotificationConfig(BaseModel):
    """
    Attributes:
        topic (Literal['tasking:order_status']): Notification topic.
        email (Union[None, bool]): Opted into email notifications. Default: False.
    """

    topic: Literal["tasking:order_status"] = Field(
        "tasking:order_status", description="Notification topic.", alias="topic"
    )
    email: Union[None, bool] = Field(
        False, description="Opted into email notifications.", alias="email"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
