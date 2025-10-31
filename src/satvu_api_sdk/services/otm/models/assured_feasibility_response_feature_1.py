from __future__ import annotations

from typing import TYPE_CHECKING, Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.assured_feasibility_response_properties import (
        AssuredFeasibilityResponseProperties,
    )
    from ..models.point import Point


class AssuredFeasibilityResponseFeature1(BaseModel):
    """Object representing an assured feasibility response.

    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (AssuredFeasibilityResponseProperties): Properties of the assured priority feasibility response.
        id (UUID): The ID of the feasibility request.
        signature (str): Signature token
        bbox (list[float] | None):
    """

    type_: Literal["Feature"] = Field("Feature", description=None, alias="type")
    geometry: "Point" = Field(..., description="Point Model", alias="geometry")
    properties: "AssuredFeasibilityResponseProperties" = Field(
        ...,
        description="Properties of the assured priority feasibility response.",
        alias="properties",
    )
    id: UUID = Field(..., description="The ID of the feasibility request.", alias="id")
    signature: str = Field(..., description="Signature token", alias="signature")
    bbox: list[float] | None = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
