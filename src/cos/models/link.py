from typing import Union

from pydantic import BaseModel

from ..models.link_body_type_0 import LinkBodyType0
from ..models.link_method import LinkMethod


class Link(BaseModel):
    """Inherits from the latest Links object defined in the event schema registry.

    Attributes:
        href (str): The actual link in the format of an URL. Relative and absolute links are both allowed.
        rel (str): Relationship between the current document and the linked document.
        type (str): Media type of the referenced entity.
        title (Union[None, str]): A human readable title to be used in rendered displays of the link.
        method (Union[None, LinkMethod]): The HTTP method of the request. Default: LinkMethod.GET.
        body (Union[LinkBodyType0, None]): A JSON object containing fields/values that must be included in the body of
            the next request.
        merge (Union[None, bool]): If `true`, the headers/body fields in the `next` link must be merged into the
            original request and be sent combined in the next request. Default: False.
    """

    href: str
    rel: str
    type: str
    title: Union[None, str] = None
    method: Union[None, LinkMethod] = LinkMethod.GET
    body: Union[LinkBodyType0, None] = None
    merge: Union[None, bool] = False

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "href",
            "rel",
            "type",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "href": str,
            "rel": str,
            "type": str,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "title": object,
            "method": object,
            "body": object,
            "merge": bool,
        }
