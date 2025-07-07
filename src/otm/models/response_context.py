from pydantic import BaseModel


class ResponseContext(BaseModel):
    """
    Attributes:
        limit (int): Applied per page item limit.
        matched (int): Total number of results.
        returned (int): Number of returned items in page.
    """

    limit: int
    matched: int
    returned: int
