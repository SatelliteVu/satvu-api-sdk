from pydantic import BaseModel, Field


class ResponseContext(BaseModel):
    """Contextual information for pagination responses

    Attributes:
        limit (int): Applied per page results limit.
        matched (int): Total number of results.
        returned (int): Number of returned users in page.
    """

    limit: int = Field(..., description="Applied per page results limit.")
    matched: int = Field(..., description="Total number of results.")
    returned: int = Field(..., description="Number of returned users in page.")
