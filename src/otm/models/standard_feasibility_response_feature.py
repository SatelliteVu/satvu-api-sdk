from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.geo_json_point import GeoJSONPoint
    from ..models.standard_feasibility_response_properties import (
        StandardFeasibilityResponseProperties,
    )


class StandardFeasibilityResponseFeature(BaseModel):
    """Object representing a standard feasibility response.

    Attributes:
        type_ (Literal['Feature']):
        geometry (GeoJSONPoint):
        properties (StandardFeasibilityResponseProperties): Properties of the standard priority feasibility response.
        id (UUID): The ID of the feasibility request.
        bbox (Union[None, list[float]]):
    """

    type_: Literal["Feature"] = Field("Feature", description=None, alias="type")
    geometry: "GeoJSONPoint" = Field(..., description=None, alias="geometry")
    properties: "StandardFeasibilityResponseProperties" = Field(
        ...,
        description="Properties of the standard priority feasibility response.",
        alias="properties",
    )
    id: UUID = Field(..., description="The ID of the feasibility request.", alias="id")
    bbox: Union[None, list[float]] = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
