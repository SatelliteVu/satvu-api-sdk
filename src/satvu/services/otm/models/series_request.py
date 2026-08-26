# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.point import Point
    from ..models.series_properties import SeriesProperties


class SeriesRequest(BaseModel):
    """Request body for creating a recurring tasking series.

    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (SeriesProperties): Properties for a series creation request.

            Provide either total_order_count or end_date to specify the series length.
        reseller_end_user_id (None | UUID): End user UUID — required when the contract is a reseller contract.
    """

    type_: Literal["Feature"] = Field(default="Feature", description=None, alias="type")
    geometry: Point = Field(..., description="""Point Model""", alias="geometry")
    properties: SeriesProperties = Field(
        ...,
        description="""Properties for a series creation request.

Provide either total_order_count or end_date to specify the series length.""",
        alias="properties",
    )
    reseller_end_user_id: None | UUID = Field(
        default=None,
        description="""End user UUID — required when the contract is a reseller contract.""",
        alias="reseller_end_user_id",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
