from typing import TypedDict


class Link(TypedDict):
    """
    Attributes:
        href (str): The link in the format of a URL.
        rel (str): The relationship between the current document and the linked document.
    """

    href: str
    rel: str
