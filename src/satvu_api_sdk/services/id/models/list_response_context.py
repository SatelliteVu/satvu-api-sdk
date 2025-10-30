from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ListResponseContext(BaseModel):
    """
    Attributes:
        per_page (int): Applied per page webhook limit.
        matched (int): Total number of results.
        returned (int): Number of returned webhooks in page.
    """

    per_page: int = Field(
        ..., description="Applied per page webhook limit.", alias="per_page"
    )
    matched: int = Field(..., description="Total number of results.", alias="matched")
    returned: int = Field(
        ..., description="Number of returned webhooks in page.", alias="returned"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
