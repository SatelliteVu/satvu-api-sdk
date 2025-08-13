from pydantic import BaseModel, ConfigDict, Field


class NotificationDescription(BaseModel):
    """
    Attributes:
        topic (str): Notification topic.
        name (str): Name of notification type.
        description (str): Description of notification type.
    """

    topic: str = Field(..., description="Notification topic.", alias="topic")
    name: str = Field(..., description="Name of notification type.", alias="name")
    description: str = Field(
        ..., description="Description of notification type.", alias="description"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
