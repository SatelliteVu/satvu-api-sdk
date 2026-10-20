# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class ListResponseContext(pydantic.BaseModel):
    """
    Attributes:
        per_page (int): Applied per page webhook limit.
        matched (int): Total number of results.
        returned (int): Number of returned webhooks in page.
    """

    per_page: int = pydantic.Field(
        ..., description="""Applied per page webhook limit.""", alias="per_page"
    )
    matched: int = pydantic.Field(
        ..., description="""Total number of results.""", alias="matched"
    )
    returned: int = pydantic.Field(
        ..., description="""Number of returned webhooks in page.""", alias="returned"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
