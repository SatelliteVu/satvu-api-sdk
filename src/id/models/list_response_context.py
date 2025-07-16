from pydantic import BaseModel, Field


class ListResponseContext(BaseModel):
    """
    Attributes:
        per_page (int): Applied per page webhook limit.
        matched (int): Total number of results.
        returned (int): Number of returned webhooks in page.
    """

    per_page: int = Field(..., description="Applied per page webhook limit.")
    matched: int = Field(..., description="Total number of results.")
    returned: int = Field(..., description="Number of returned webhooks in page.")
