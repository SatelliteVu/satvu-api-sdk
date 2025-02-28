from typing import Literal, TypedDict, Union

from ..types import Unset


class NotificationConfig(TypedDict):
    """
    Attributes:
        topic (Literal['tasking:order_status']): Notification topic.
        email (Union[Unset, bool]): Opted into email notifications. Default: False.
    """

    topic: Literal["tasking:order_status"]
    email: Union[Unset, bool] = False
