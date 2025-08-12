from pydantic import BaseModel, ConfigDict, Field


class ResponseContext(BaseModel):
    """
    Attributes:
        limit (int): Applied per page item limit.
        matched (int): Total number of results.
        returned (int): Number of returned items in page.
    """

    limit: int = Field(..., description="Applied per page item limit.", alias="limit")
    matched: int = Field(..., description="Total number of results.", alias="matched")
    returned: int = Field(
        ..., description="Number of returned items in page.", alias="returned"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
