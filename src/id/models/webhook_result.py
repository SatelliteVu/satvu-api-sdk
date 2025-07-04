from dataclasses import dataclass
from typing import Union

from ..models.webhook_failure_title import WebhookFailureTitle


@dataclass
class WebhookResult:
    """
    Attributes:
        success (bool): Whether the request to the webhook URL was successful.
        status_code (Union[None, int]): The HTTP status code responded by the webhook URL, if applicable.
        title (Union[None, WebhookFailureTitle]): The cause of the test failure, if applicable.
        detail (Union[None, str]): Detail about why the test failed, if applicable.
    """

    success: bool
    status_code: Union[None, int] = None
    title: Union[None, WebhookFailureTitle] = None
    detail: Union[None, str] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "success",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "success": bool,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "status_code": object,
            "title": object,
            "detail": object,
        }
