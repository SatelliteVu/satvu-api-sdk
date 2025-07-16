from pydantic import BaseModel, Field


class ResponseContext(BaseModel):
    """
    Attributes:
        limit (int): Applied per page item limit.
        matched (int): Total number of results.
        returned (int): Number of returned items in page.
    """

    limit: int = Field(..., description="Applied per page item limit.")
    matched: int = Field(..., description="Total number of results.")
    returned: int = Field(..., description="Number of returned items in page.")
