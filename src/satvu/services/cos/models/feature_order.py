# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.order import Order
    from ..models.point_geometry import PointGeometry
    from ..models.polygon_geometry import PolygonGeometry


class FeatureOrder(BaseModel):
    """
    Attributes:
        id (str | UUID): The unique identifier of the feature.
        type_ (Literal['Feature']):  Default: 'Feature'.
        geometry (Union['PointGeometry', 'PolygonGeometry', None]): Defines the full footprint of the asset represented
            by this feature.
        properties (Union['Order', None]): A map of additional metadata for the feature.
    """

    id: str | UUID = Field(
        ..., description="""The unique identifier of the feature.""", alias="id"
    )
    type_: Literal["Feature"] = Field(default="Feature", description=None, alias="type")
    geometry: Union[PointGeometry, PolygonGeometry, None] = Field(
        default=None,
        description="""Defines the full footprint of the asset represented by this feature.""",
        alias="geometry",
    )
    properties: Union[Order, None] = Field(
        default=None,
        description="""A map of additional metadata for the feature.""",
        alias="properties",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
