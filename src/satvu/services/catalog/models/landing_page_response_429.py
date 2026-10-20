# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class LandingPageResponse429(pydantic.BaseModel):
    """
    Attributes:
        code (str): Error code Example: TooManyRequests.
        description (str): Error description Example: Rate limit exceeded. Please try again later..
    """

    code: str = pydantic.Field(..., description="""Error code""", alias="code")
    description: str = pydantic.Field(
        ..., description="""Error description""", alias="description"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
