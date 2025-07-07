from typing import Union

from pydantic import BaseModel

from ..models.webhook_failure_title import WebhookFailureTitle


class WebhookResult(BaseModel):
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
