from typing import TypedDict


class ListResponseContext(TypedDict):
    """
    Attributes:
        per_page (int): Applied per page webhook limit.
        matched (int): Total number of results.
        returned (int): Number of returned webhooks in page.
    """

    per_page: int
    matched: int
    returned: int
