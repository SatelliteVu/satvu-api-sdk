from typing import Literal, TypedDict, Union

from ..types import Unset


class NotificationSettings(TypedDict):
    """
    Attributes:
        topic (Literal['tasking:order_status']): Notification topic.
        name (str): Name of notification type.
        description (str): Description of notification type.
        email (Union[Unset, bool]): Opted into email notifications. Default: False.
    """

    topic: Literal["tasking:order_status"]
    name: str
    description: str
    email: Union[Unset, bool] = False
