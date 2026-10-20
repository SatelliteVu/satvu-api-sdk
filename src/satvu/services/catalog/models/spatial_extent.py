# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class SpatialExtent(pydantic.BaseModel):
    """Potential spatial extents covered by the Collection.

    Attributes:
        bbox (list[list[float]]): Potential spatial extents covered by the Collection.
    """

    bbox: list[list[float]] = pydantic.Field(
        ...,
        description="""Potential spatial extents covered by the Collection.""",
        alias="bbox",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
