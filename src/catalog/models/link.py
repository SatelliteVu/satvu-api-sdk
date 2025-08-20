from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.link_body import LinkBody


class Link(BaseModel):
    """
    Attributes:
        href (str): The actual link in the format of an URL. Example: http://example.com.
        merge (Union[None, bool]): If true, the body fields in the next link must be merged into the original request
            and be sent combined in the next request.
        method (str): The HTTP method of the request, either GET or POST. Example: GET.
        rel (str): The relationship between the current document and the linked document. Example: parent.
        body (Union[None, LinkBody]): A JSON object containing fields/values that must by included in the body of the
            next request.
        title (Union[None, str]): The title of the link. Example: Example Link.
        type_ (Union[None, str]): Media type of the referenced entity. Example: application/geo+json.
    """

    href: str = Field(
        ..., description="The actual link in the format of an URL.", alias="href"
    )
    merge: Union[None, bool] = Field(
        ...,
        description="If true, the body fields in the next link must be merged into the original request and be sent combined in the next request.",
        alias="merge",
    )
    method: str = Field(
        ...,
        description="The HTTP method of the request, either GET or POST.",
        alias="method",
    )
    rel: str = Field(
        ...,
        description="The relationship between the current document and the linked document.",
        alias="rel",
    )
    body: Union[None, "LinkBody"] = Field(
        None,
        description="A JSON object containing fields/values that must by included in the body of the next request.",
        alias="body",
    )
    title: Union[None, str] = Field(
        None, description="The title of the link.", alias="title"
    )
    type_: Union[None, str] = Field(
        None, description="Media type of the referenced entity.", alias="type"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
