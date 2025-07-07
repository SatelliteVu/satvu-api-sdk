from pydantic import BaseModel


class ResponseContext(BaseModel):
    """Contextual information for pagination responses

    Attributes:
        limit (int): Applied per page results limit.
        matched (int): Total number of results.
        returned (int): Number of returned users in page.
    """

    limit: int
    matched: int
    returned: int
