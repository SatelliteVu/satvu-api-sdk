from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.link_method import LinkMethod

if TYPE_CHECKING:
    from ..models.link_body_type_0 import LinkBodyType0


class Link(BaseModel):
    """Inherits from the latest Links object defined in the event schema registry.

    Attributes:
        href (str): The actual link in the format of an URL. Relative and absolute links are both allowed.
        rel (str): Relationship between the current document and the linked document.
        type_ (str): Media type of the referenced entity.
        title (None | str): A human readable title to be used in rendered displays of the link.
        method (Union[None, 'LinkMethod']): The HTTP method of the request. Default: LinkMethod.GET.
        body (Union['LinkBodyType0', None]): A JSON object containing fields/values that must be included in the body of
            the next request.
        merge (Union[None, bool]): If `true`, the headers/body fields in the `next` link must be merged into the
            original request and be sent combined in the next request. Default: False.
    """

    href: str = Field(
        ...,
        description="The actual link in the format of an URL. Relative and absolute links are both allowed.",
        alias="href",
    )
    rel: str = Field(
        ...,
        description="Relationship between the current document and the linked document.",
        alias="rel",
    )
    type_: str = Field(
        ..., description="Media type of the referenced entity.", alias="type"
    )
    title: None | str = Field(
        None,
        description="A human readable title to be used in rendered displays of the link.",
        alias="title",
    )
    method: Union[None, "LinkMethod"] = Field(
        LinkMethod.GET, description="The HTTP method of the request.", alias="method"
    )
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

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
