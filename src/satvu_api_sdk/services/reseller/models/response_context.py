from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ResponseContext(BaseModel):
    """Contextual information for pagination responses

    Attributes:
        limit (int): Applied per page results limit.
        matched (int): Total number of results.
        returned (int): Number of returned users in page.
    """

    limit: int = Field(
        ..., description="Applied per page results limit.", alias="limit"
    )
    matched: int = Field(..., description="Total number of results.", alias="matched")
    returned: int = Field(
        ..., description="Number of returned users in page.", alias="returned"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
