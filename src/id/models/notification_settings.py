from typing import Literal, Union

from pydantic import BaseModel


class NotificationSettings(BaseModel):
    """
    Attributes:
        topic (Literal['tasking:order_status']): Notification topic.
        name (str): Name of notification type.
        description (str): Description of notification type.
        email (Union[None, bool]): Opted into email notifications. Default: False.
    """

    topic: Literal["tasking:order_status"]
    name: str
    description: str
    email: Union[None, bool] = False
