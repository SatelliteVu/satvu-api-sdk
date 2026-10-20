# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from uuid import UUID

import pydantic


class SearchRequest(pydantic.BaseModel):
    """
    Attributes:
        token (None | str): Pagination token.
        limit (int | None): Number of items to return per page. Default: 25.
        order_ids (list[UUID] | None): A list of IDs.
    """

    token: None | str = pydantic.Field(
        default=None, description="""Pagination token.""", alias="token"
    )
    limit: int | None = pydantic.Field(
        default=25, description="""Number of items to return per page.""", alias="limit"
    )
    order_ids: list[UUID] | None = pydantic.Field(
        default=None, description="""A list of IDs.""", alias="order_ids"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
