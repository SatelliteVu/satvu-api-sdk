from dataclasses import dataclass
from typing import Literal, Union

from ..types import Unset


@dataclass
class NotificationSettings:
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

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "topic",
            "name",
            "description",
        }
