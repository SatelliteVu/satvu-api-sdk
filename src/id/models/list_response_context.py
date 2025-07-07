from pydantic import BaseModel


class ListResponseContext(BaseModel):
    """
    Attributes:
        per_page (int): Applied per page webhook limit.
        matched (int): Total number of results.
        returned (int): Number of returned webhooks in page.
    """

    per_page: int
    matched: int
    returned: int
