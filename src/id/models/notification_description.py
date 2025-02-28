from typing import Literal, TypedDict


class NotificationDescription(TypedDict):
    """
    Attributes:
        topic (Literal['tasking:order_status']): Notification topic.
        name (str): Name of notification type.
        description (str): Description of notification type.
    """

    topic: Literal["tasking:order_status"]
    name: str
    description: str
