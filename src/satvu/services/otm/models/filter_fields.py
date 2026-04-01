# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class FilterFields(BaseModel):
    """
    Attributes:
        status (list[str] | None | str):
        min_off_nadir (int | list[int] | None):
        max_off_nadir (int | list[int] | None):
    """

    status: list[str] | None | str = Field(
        default=None, description=None, alias="status"
    )
    min_off_nadir: int | list[int] | None = Field(
        default=None, description=None, alias="min_off_nadir"
    )
    max_off_nadir: int | list[int] | None = Field(
        default=None, description=None, alias="max_off_nadir"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
