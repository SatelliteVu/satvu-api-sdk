# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

import pydantic

from ..models.webhook_failure_title import WebhookFailureTitle


class WebhookResult(pydantic.BaseModel):
    """
    Attributes:
        success (bool): Whether the request to the webhook URL was successful.
        status_code (int | None): The HTTP status code responded by the webhook URL, if applicable.
        title (Union['WebhookFailureTitle', None]): The cause of the test failure, if applicable.
        detail (None | str): Detail about why the test failed, if applicable.
    """

    success: bool = pydantic.Field(
        ...,
        description="""Whether the request to the webhook URL was successful.""",
        alias="success",
    )
    status_code: int | None = pydantic.Field(
        default=None,
        description="""The HTTP status code responded by the webhook URL, if applicable.""",
        alias="status_code",
    )
    title: Union[WebhookFailureTitle, None] = pydantic.Field(
        default=None,
        description="""The cause of the test failure, if applicable.""",
        alias="title",
    )
    detail: None | str = pydantic.Field(
        default=None,
        description="""Detail about why the test failed, if applicable.""",
        alias="detail",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
