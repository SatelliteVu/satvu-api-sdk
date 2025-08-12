from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from ..models.point import Point
from ..models.standard_feasibility_response_properties import (
    StandardFeasibilityResponseProperties,
)


class StandardFeasibilityResponseFeature(BaseModel):
    """Object representing a standard feasibility response.

    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (StandardFeasibilityResponseProperties): Properties of the standard priority feasibility response.
        id (UUID): The ID of the feasibility request.
        bbox (Union[None, list[float]]):
    """

    type_: Literal["Feature"] = Field("Feature", description=None, alias="type")
    geometry: "Point" = Field(..., description="Point Model", alias="geometry")
    properties: "StandardFeasibilityResponseProperties" = Field(
        ...,
        description="Properties of the standard priority feasibility response.",
        alias="properties",
    )
    id: UUID = Field(..., description="The ID of the feasibility request.", alias="id")
    bbox: Union[None, list[float]] = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
