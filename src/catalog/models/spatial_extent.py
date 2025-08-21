from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class SpatialExtent(BaseModel):
    """Potential spatial extents covered by the Collection.

    Attributes:
        bbox (list[list[float]]): Potential spatial extents covered by the Collection.
    """

    bbox: list[list[float]] = Field(
        ...,
        description="Potential spatial extents covered by the Collection.",
        alias="bbox",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
