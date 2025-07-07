from typing import Union

from pydantic import BaseModel

from ..models.link_body_type_0 import LinkBodyType0
from ..models.request_method import RequestMethod


class Link(BaseModel):
    """
    Attributes:
        href (str): The link in the format of a URL.
        rel (str): The relationship between the current document and the linked document.
        method (Union[None, RequestMethod]):
        body (Union[LinkBodyType0, None]): A JSON object containing fields/values that must be included in the body of
            the next request.
        merge (Union[None, bool]): If `true`, the headers/body fields in the `next` link must be merged into the
            original request and be sent combined in the next request. Default: False.
        type (Union[None, str]): The media type of the referenced entity.
        title (Union[None, str]): Title of the link
    """

    href: str
    rel: str
    method: Union[None, RequestMethod] = None
    body: Union[LinkBodyType0, None] = None
    merge: Union[None, bool] = False
    type: Union[None, str] = None
    title: Union[None, str] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "href",
            "rel",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "href": str,
            "rel": str,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "method": object,
            "body": object,
            "merge": bool,
            "type": object,
            "title": object,
        }
