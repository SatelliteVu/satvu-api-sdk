from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.spatial_extent import SpatialExtent
    from ..models.temporal_extent import TemporalExtent


class Extent(BaseModel):
    """Spatial and temporal extents.

    Attributes:
        spatial (SpatialExtent): Potential spatial extents covered by the Collection.
        temporal (TemporalExtent): Potential temporal extents covered by the Collection.
    """

    spatial: "SpatialExtent" = Field(
        ...,
        description="Potential spatial extents covered by the Collection.",
        alias="spatial",
    )
    temporal: "TemporalExtent" = Field(
        ...,
        description="Potential temporal extents covered by the Collection.",
        alias="temporal",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
