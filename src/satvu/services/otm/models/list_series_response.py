# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.response_context import ResponseContext
    from ..models.stored_series_response import StoredSeriesResponse


class ListSeriesResponse(BaseModel):
    """Paginated list of series.

    Attributes:
        type_ (Literal['FeatureCollection']):
        features (list[StoredSeriesResponse]): List of series.
        links (list[Link]): Links to previous and/or next page.
        context (ResponseContext): Context about the response.
        bbox (list[float] | None):
    """

    type_: Literal["FeatureCollection"] = Field(
        default="FeatureCollection", description=None, alias="type"
    )
    features: list[StoredSeriesResponse] = Field(
        ..., description="""List of series.""", alias="features"
    )
    links: list[Link] = Field(
        ..., description="""Links to previous and/or next page.""", alias="links"
    )
    context: ResponseContext = Field(
        ..., description="""Context about the response.""", alias="context"
    )
    bbox: list[float] | None = Field(default=None, description=None, alias="bbox")

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
