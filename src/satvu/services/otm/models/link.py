# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.request_method import RequestMethod


class Link(BaseModel):
    """
    Attributes:
        href (str): The link in the format of a URL.
        rel (str): The relationship between the current document and the linked document.
        method (Union[None, 'RequestMethod']):
        body (dict | None): A JSON object containing fields/values that must be included in the body of the next
            request.
        merge (Union[None, bool]): If `true`, the headers/body fields in the `next` link must be merged into the
            original request and be sent combined in the next request. Default: False.
        type_ (None | str): The media type of the referenced entity.
        title (None | str): Title of the link.
    """

    href: str = Field(
        ..., description="""The link in the format of a URL.""", alias="href"
    )
    rel: str = Field(
        ...,
        description="""The relationship between the current document and the linked document.""",
        alias="rel",
    )
    method: Union[None, RequestMethod] = Field(
        default=None, description=None, alias="method"
    )
    body: dict | None = Field(
        default=None,
        description="""A JSON object containing fields/values that must be included in the body of the next request.""",
        alias="body",
    )
    merge: Union[None, bool] = Field(
        default=False,
        description="""If `true`, the headers/body fields in the `next` link must be merged into the original request and be sent combined in the next request.""",
        alias="merge",
    )
    type_: None | str = Field(
        default=None,
        description="""The media type of the referenced entity.""",
        alias="type",
    )
    title: None | str = Field(
        default=None, description="""Title of the link.""", alias="title"
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
