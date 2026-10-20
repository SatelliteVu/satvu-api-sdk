# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

import pydantic


class Link(pydantic.BaseModel):
    """
    Attributes:
        href (str): The actual link in the format of an URL. Example: http://example.com.
        method (str): The HTTP method of the request, either GET or POST. Example: GET.
        rel (str): The relationship between the current document and the linked document. Example: parent.
        body (Union[None, dict]): A JSON object containing fields/values that must be included in the body of the next
            request.
        merge (bool | None): If true, the body fields in the next link must be merged into the original request and be
            sent combined in the next request.
        title (Union[None, str]): The title of the link. Example: Example Link.
        type_ (Union[None, str]): Media type of the referenced entity. Example: application/geo+json.
    """

    href: str = pydantic.Field(
        ..., description="""The actual link in the format of an URL.""", alias="href"
    )
    method: str = pydantic.Field(
        ...,
        description="""The HTTP method of the request, either GET or POST.""",
        alias="method",
    )
    rel: str = pydantic.Field(
        ...,
        description="""The relationship between the current document and the linked document.""",
        alias="rel",
    )
    body: Union[None, dict] = pydantic.Field(
        default=None,
        description="""A JSON object containing fields/values that must be included in the body of the next request.""",
        alias="body",
    )
    merge: bool | None = pydantic.Field(
        default=None,
        description="""If true, the body fields in the next link must be merged into the original request and be sent combined in the next request.""",
        alias="merge",
    )
    title: Union[None, str] = pydantic.Field(
        default=None, description="""The title of the link.""", alias="title"
    )
    type_: Union[None, str] = pydantic.Field(
        default=None,
        description="""Media type of the referenced entity.""",
        alias="type",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
