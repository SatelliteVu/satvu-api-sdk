# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import pydantic

if TYPE_CHECKING:
    from ..models.point import Point
    from ..models.stored_series_properties import StoredSeriesProperties


class StoredSeriesResponse(pydantic.BaseModel):
    """Response body for a stored recurring tasking series.

    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (StoredSeriesProperties): Properties returned in a series response.
        bbox (list[float] | None):
        id (float | int | None | str):
    """

    type_: Literal["Feature"] = pydantic.Field(
        default="Feature", description=None, alias="type"
    )
    geometry: Point = pydantic.Field(
        ..., description="""Point Model""", alias="geometry"
    )
    properties: StoredSeriesProperties = pydantic.Field(
        ...,
        description="""Properties returned in a series response.""",
        alias="properties",
    )
    bbox: list[float] | None = pydantic.Field(
        default=None, description=None, alias="bbox"
    )
    id: float | int | None | str = pydantic.Field(
        default=None, description=None, alias="id"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
