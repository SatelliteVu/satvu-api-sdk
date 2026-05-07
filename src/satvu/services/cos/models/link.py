# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.method import Method


class Link(BaseModel):
    """Navigation link to related resources with support for pagination and API navigation.

    Attributes:
        href (str): The actual link in the format of an URL. Relative and absolute links are both allowed.
        rel (str): Relationship between the current document and the linked document.
        type_ (str): Media type of the referenced entity.
        title (None | str): A human readable title to be used in rendered displays of the link.
        method (Union[None, 'Method']): The HTTP method of the request. Default: Method.GET.
        body (dict | None): A JSON object containing fields/values that must be included in the body of the next
            request.
        merge (Union[None, bool]): If `true`, the headers/body fields in the `next` link must be merged into the
            original request and be sent combined in the next request. Default: False.
    """

    href: str = Field(
        ...,
        description="""The actual link in the format of an URL. Relative and absolute links are both allowed.""",
        alias="href",
    )
    rel: str = Field(
        ...,
        description="""Relationship between the current document and the linked document.""",
        alias="rel",
    )
    type_: str = Field(
        ..., description="""Media type of the referenced entity.""", alias="type"
    )
    title: None | str = Field(
        default=None,
        description="""A human readable title to be used in rendered displays of the link.""",
        alias="title",
    )
    method: Union[None, Method] = Field(
        default=Method.GET,
        description="""The HTTP method of the request.""",
        alias="method",
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

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
