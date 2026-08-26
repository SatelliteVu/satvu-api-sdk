# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.point import Point
    from ..models.stored_series_properties import StoredSeriesProperties


class StoredSeriesResponse(BaseModel):
    """Response body for a stored recurring tasking series.

    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (StoredSeriesProperties): Properties returned in a series response.
        bbox (list[float] | None):
        id (int | None | str):
    """

    type_: Literal["Feature"] = Field(default="Feature", description=None, alias="type")
    geometry: Point = Field(..., description="""Point Model""", alias="geometry")
    properties: StoredSeriesProperties = Field(
        ...,
        description="""Properties returned in a series response.""",
        alias="properties",
    )
    bbox: list[float] | None = Field(default=None, description=None, alias="bbox")
    id: int | None | str = Field(default=None, description=None, alias="id")

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
