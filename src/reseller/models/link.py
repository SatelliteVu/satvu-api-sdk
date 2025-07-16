from typing import Union

from pydantic import BaseModel, Field

from ..models.link_body_type_0 import LinkBodyType0
from ..models.request_method import RequestMethod


class Link(BaseModel):
    """
    Attributes:
        href (str): The link in the format of a URL.
        rel (str): The relationship between the current document and the linked document.
        title (str): Title of the link.
        method (Union[None, RequestMethod]):
        body (Union[LinkBodyType0, None]): A JSON object containing fields/values that must be included in the body of
            the next request.
        merge (Union[None, bool]): If `true`, the headers/body fields in the `next` link must be merged into the
            original request and be sent combined in the next request. Default: False.
        type (Union[None, str]): The media type of the referenced entity.
    """

    href: str = Field(..., description="The link in the format of a URL.")
    rel: str = Field(
        ...,
        description="The relationship between the current document and the linked document.",
    )
    title: str = Field(..., description="Title of the link.")
    method: Union[None, RequestMethod] = Field(None, description=None)
    body: Union[LinkBodyType0, None] = Field(
        None,
        description="A JSON object containing fields/values that must be included in the body of the next request.",
    )
    merge: Union[None, bool] = Field(
        False,
        description="If `true`, the headers/body fields in the `next` link must be merged into the original request and be sent combined in the next request.",
    )
    type: Union[None, str] = Field(
        None, description="The media type of the referenced entity."
    )
