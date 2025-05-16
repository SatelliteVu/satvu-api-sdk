from typing import TYPE_CHECKING, TypedDict, Union

from ..models.link_method import LinkMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_body_type_0 import LinkBodyType0


class Link(TypedDict):
    """Inherits from the latest Links object defined in the event schema registry.

    Attributes:
        href (str): The actual link in the format of an URL. Relative and absolute links are both allowed.
        rel (str): Relationship between the current document and the linked document.
        type_ (str): Media type of the referenced entity.
        title (Union[None, Unset, str]): A human readable title to be used in rendered displays of the link.
        method (Union[Unset, LinkMethod]): The HTTP method of the request. Default: LinkMethod.GET.
        body (Union['LinkBodyType0', None, Unset]): A JSON object containing fields/values that must be included in the
            body of the next request.
        merge (Union[Unset, bool]): If `true`, the headers/body fields in the `next` link must be merged into the
            original request and be sent combined in the next request. Default: False.
    """

    href: str
    rel: str
    type_: str
    title: Union[None, Unset, str] = UNSET
    method: Union[Unset, LinkMethod] = LinkMethod.GET
    body: Union["LinkBodyType0", None, Unset] = UNSET
    merge: Union[Unset, bool] = False
