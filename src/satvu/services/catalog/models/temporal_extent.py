# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Any

import pydantic


class TemporalExtent(pydantic.BaseModel):
    """Potential temporal extents covered by the Collection.

    Attributes:
        interval (list[Any]): Potential temporal extents covered by the Collection.
    """

    interval: list[Any] = pydantic.Field(
        ...,
        description="""Potential temporal extents covered by the Collection.""",
        alias="interval",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
