# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class LegacyLink(BaseModel):
    """Related resources and navigation links (legacy STAC v0.9 format).

    Attributes:
        href (str):
        rel (str):
        type_ (None | str):
        title (None | str):
    """

    href: str = Field(..., description=None, alias="href")
    rel: str = Field(..., description=None, alias="rel")
    type_: None | str = Field(default=None, description=None, alias="type")
    title: None | str = Field(default=None, description=None, alias="title")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
