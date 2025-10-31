from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.webhook_failure_title import WebhookFailureTitle


class WebhookResult(BaseModel):
    """
    Attributes:
        success (bool): Whether the request to the webhook URL was successful.
        status_code (int | None): The HTTP status code responded by the webhook URL, if applicable.
        title (Union['WebhookFailureTitle', None]): The cause of the test failure, if applicable.
        detail (None | str): Detail about why the test failed, if applicable.
    """

    success: bool = Field(
        ...,
        description="Whether the request to the webhook URL was successful.",
        alias="success",
    )
    status_code: int | None = Field(
        None,
        description="The HTTP status code responded by the webhook URL, if applicable.",
        alias="status_code",
    )
    title: Union["WebhookFailureTitle", None] = Field(
        None, description="The cause of the test failure, if applicable.", alias="title"
    )
    detail: None | str = Field(
        None,
        description="Detail about why the test failed, if applicable.",
        alias="detail",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
