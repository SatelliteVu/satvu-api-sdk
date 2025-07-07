from typing import Literal, Union

from pydantic import BaseModel


class NotificationConfig(BaseModel):
    """
    Attributes:
        topic (Literal['tasking:order_status']): Notification topic.
        email (Union[None, bool]): Opted into email notifications. Default: False.
    """

    topic: Literal["tasking:order_status"]
    email: Union[None, bool] = False
