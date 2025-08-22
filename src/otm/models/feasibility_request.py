from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.assured_feasibility_fields import AssuredFeasibilityFields
    from ..models.point import Point
    from ..models.standard_request_properties import StandardRequestProperties


class FeasibilityRequest(BaseModel):
    """Payload for feasibility request.

    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union['AssuredFeasibilityFields', 'StandardRequestProperties']): A map of additional metadata about
            the requested image.
    """

    type_: Literal["Feature"] = Field("Feature", description=None, alias="type")
    geometry: "Point" = Field(..., description="Point Model", alias="geometry")
    properties: Union["AssuredFeasibilityFields", "StandardRequestProperties"] = Field(
        ...,
        description="A map of additional metadata about the requested image.",
        alias="properties",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
