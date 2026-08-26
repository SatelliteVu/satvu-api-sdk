# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class GetSearchResponse429(BaseModel):
    """
    Attributes:
        code (str): Error code Example: TooManyRequests.
        description (str): Error description Example: Rate limit exceeded. Please try again later..
    """

    code: str = Field(..., description="""Error code""", alias="code")
    description: str = Field(
        ..., description="""Error description""", alias="description"
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
