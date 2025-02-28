from typing import TypedDict, Union

from ..models.webhook_failure_title import WebhookFailureTitle
from ..types import UNSET, Unset


class WebhookResult(TypedDict):
    """
    Attributes:
        success (bool): Whether the request to the webhook URL was successful.
        status_code (Union[None, Unset, int]): The HTTP status code responded by the webhook URL, if applicable.
        title (Union[None, Unset, WebhookFailureTitle]): The cause of the test failure, if applicable.
        detail (Union[None, Unset, str]): Detail about why the test failed, if applicable.
    """

    success: bool
    status_code: Union[None, Unset, int] = UNSET
    title: Union[None, Unset, WebhookFailureTitle] = UNSET
    detail: Union[None, Unset, str] = UNSET
