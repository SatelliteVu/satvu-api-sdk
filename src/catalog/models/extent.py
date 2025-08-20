from pydantic import BaseModel, ConfigDict, Field

from ..models.spatial_extent import SpatialExtent
from ..models.types_temporal_extent import TypesTemporalExtent


class Extent(BaseModel):
    """Spatial and temporal extents.

    Attributes:
        spatial (SpatialExtent): Potential spatial extents covered by the Collection.
        temporal (TypesTemporalExtent): Potential temporal extents covered by the Collection.
    """

    spatial: "SpatialExtent" = Field(
        ...,
        description="Potential spatial extents covered by the Collection.",
        alias="spatial",
    )
    temporal: "TypesTemporalExtent" = Field(
        ...,
        description="Potential temporal extents covered by the Collection.",
        alias="temporal",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
