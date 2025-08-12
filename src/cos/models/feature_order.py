from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from ..models.order import Order
from ..models.point_geometry import PointGeometry
from ..models.polygon_geometry import PolygonGeometry


class FeatureOrder(BaseModel):
    """
    Attributes:
        id (Union[UUID, str]): The unique identifier of the item within the order.
        type_ (Union[Literal['Feature'], None]):  Default: 'Feature'.
        geometry (Union[None, PointGeometry, PolygonGeometry]): Defines the full footprint of the asset represented by
            the item.
        properties (Union[None, Order]): A dictionary of additional metadata for the item.
    """

    id: Union[UUID, str] = Field(
        ...,
        description="The unique identifier of the item within the order.",
        alias="id",
    )
    type_: Union[Literal["Feature"], None] = Field(
        "Feature", description=None, alias="type"
    )
    geometry: Union[None, PointGeometry, PolygonGeometry] = Field(
        None,
        description="Defines the full footprint of the asset represented by the item.",
        alias="geometry",
    )
    properties: Union[None, Order] = Field(
        None,
        description="A dictionary of additional metadata for the item.",
        alias="properties",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
