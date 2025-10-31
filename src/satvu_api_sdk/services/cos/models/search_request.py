from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class SearchRequest(BaseModel):
    """
    Attributes:
        token (None | str): Pagination token.
        limit (int | None): Number of items to return per page. Default: 25.
        order_ids (list[UUID] | None): A list of IDs.
    """

    token: None | str = Field(None, description="Pagination token.", alias="token")
    limit: int | None = Field(
        25, description="Number of items to return per page.", alias="limit"
    )
    order_ids: list[UUID] | None = Field(
        None, description="A list of IDs.", alias="order_ids"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
