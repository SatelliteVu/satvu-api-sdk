from typing import Literal

from pydantic import BaseModel


class NotificationDescription(BaseModel):
    """
    Attributes:
        topic (Literal['tasking:order_status']): Notification topic.
        name (str): Name of notification type.
        description (str): Description of notification type.
    """

    topic: Literal["tasking:order_status"]
    name: str
    description: str

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

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "topic": object,
            "name": str,
            "description": str,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
