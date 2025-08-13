from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.reseller_notification_config_topic import ResellerNotificationConfigTopic


class ResellerNotificationConfig(BaseModel):
    """
    Attributes:
        topic (ResellerNotificationConfigTopic): Notification topic.
        email (Union[None, bool]): Opted into email notifications. Default: False.
    """

    topic: ResellerNotificationConfigTopic = Field(
        ..., description="Notification topic.", alias="topic"
    )
    email: Union[None, bool] = Field(
        False, description="Opted into email notifications.", alias="email"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
