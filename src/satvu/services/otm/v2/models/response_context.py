# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class ResponseContext(pydantic.BaseModel):
    """Context about the response.

    Attributes:
        limit (int): Applied per page item limit.
        matched (int): Total number of results.
        returned (int): Number of returned items in page.
    """

    limit: int = pydantic.Field(
        ..., description="""Applied per page item limit.""", alias="limit"
    )
    matched: int = pydantic.Field(
        ..., description="""Total number of results.""", alias="matched"
    )
    returned: int = pydantic.Field(
        ..., description="""Number of returned items in page.""", alias="returned"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
