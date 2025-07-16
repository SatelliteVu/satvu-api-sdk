from typing import Union

from pydantic import BaseModel, Field

from ..models.webhook_failure_title import WebhookFailureTitle


class WebhookResult(BaseModel):
    """
    Attributes:
        success (bool): Whether the request to the webhook URL was successful.
        status_code (Union[None, int]): The HTTP status code responded by the webhook URL, if applicable.
        title (Union[None, WebhookFailureTitle]): The cause of the test failure, if applicable.
        detail (Union[None, str]): Detail about why the test failed, if applicable.
    """

    success: bool = Field(
        ..., description="Whether the request to the webhook URL was successful."
    )
    status_code: Union[None, int] = Field(
        None,
        description="The HTTP status code responded by the webhook URL, if applicable.",
    )
    title: Union[None, WebhookFailureTitle] = Field(
        None, description="The cause of the test failure, if applicable."
    )
    detail: Union[None, str] = Field(
        None, description="Detail about why the test failed, if applicable."
    )
