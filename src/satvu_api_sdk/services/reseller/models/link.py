from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.request_method import RequestMethod

if TYPE_CHECKING:
    from ..models.link_body_type_0 import LinkBodyType0


class Link(BaseModel):
    """
    Attributes:
        href (str): The link in the format of a URL.
        rel (str): The relationship between the current document and the linked document.
        title (str): Title of the link.
        method (Union[None, 'RequestMethod']):
        body (Union['LinkBodyType0', None]): A JSON object containing fields/values that must be included in the body of
            the next request.
        merge (Union[None, bool]): If `true`, the headers/body fields in the `next` link must be merged into the
            original request and be sent combined in the next request. Default: False.
        type_ (Union[None, str]): The media type of the referenced entity.
    """

    href: str = Field(..., description="The link in the format of a URL.", alias="href")
    rel: str = Field(
        ...,
        description="The relationship between the current document and the linked document.",
        alias="rel",
    )
    title: str = Field(..., description="Title of the link.", alias="title")
    method: Union[None, "RequestMethod"] = Field(None, description=None, alias="method")
    body: Union["LinkBodyType0", None] = Field(
        None,
        description="A JSON object containing fields/values that must be included in the body of the next request.",
        alias="body",
    )
    merge: Union[None, bool] = Field(
        False,
        description="If `true`, the headers/body fields in the `next` link must be merged into the original request and be sent combined in the next request.",
        alias="merge",
    )
    type_: Union[None, str] = Field(
        None, description="The media type of the referenced entity.", alias="type"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
