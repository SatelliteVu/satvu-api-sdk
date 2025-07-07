from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel

from ..models.order import Order
from ..models.point_geometry import PointGeometry
from ..models.polygon_geometry import PolygonGeometry


class FeatureOrder(BaseModel):
    """
    Attributes:
        id (Union[UUID, str]): The unique identifier of the item within the order.
        type (Union[Literal['Feature'], None]):  Default: 'Feature'.
        geometry (Union[None, PointGeometry, PolygonGeometry]): Defines the full footprint of the asset represented by
            the item.
        properties (Union[None, Order]): A dictionary of additional metadata for the item.
    """

    id: Union[UUID, str]
    type: Union[Literal["Feature"], None] = "Feature"
    geometry: Union[None, PointGeometry, PolygonGeometry] = None
    properties: Union[None, Order] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "id",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "id": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "type": object,
            "geometry": object,
            "properties": object,
        }
