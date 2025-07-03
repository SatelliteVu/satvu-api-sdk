from dataclasses import dataclass
from typing import Literal, Union

from ..types import Unset


@dataclass
class NotificationConfig:
    """
    Attributes:
        topic (Literal['tasking:order_status']): Notification topic.
        email (Union[Unset, bool]): Opted into email notifications. Default: False.
    """

    topic: Literal["tasking:order_status"]
    email: Union[Unset, bool] = False

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "topic",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "topic": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "email": bool,
        }
