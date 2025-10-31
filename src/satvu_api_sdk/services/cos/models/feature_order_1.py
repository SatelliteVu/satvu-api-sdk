from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.order_1 import Order1
    from ..models.point_geometry import PointGeometry
    from ..models.polygon_geometry import PolygonGeometry


class FeatureOrder1(BaseModel):
    """
    Attributes:
        id (str | UUID): The unique identifier of the item within the order.
        type_ (Union[Literal['Feature'], None]):  Default: 'Feature'.
        geometry (Union['PointGeometry', 'PolygonGeometry', None]): Defines the full footprint of the asset represented
            by the item.
        properties (Union['Order1', None]): A dictionary of additional metadata for the item.
    """

    id: str | UUID = Field(
        ...,
        description="The unique identifier of the item within the order.",
        alias="id",
    )
    type_: Union[Literal["Feature"], None] = Field(
        "Feature", description=None, alias="type"
    )
    geometry: Union["PointGeometry", "PolygonGeometry", None] = Field(
        None,
        description="Defines the full footprint of the asset represented by the item.",
        alias="geometry",
    )
    properties: Union["Order1", None] = Field(
        None,
        description="A dictionary of additional metadata for the item.",
        alias="properties",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
