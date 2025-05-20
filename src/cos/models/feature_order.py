from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, Union
from uuid import UUID

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order import Order
    from ..models.point_geometry import PointGeometry
    from ..models.polygon_geometry import PolygonGeometry


@dataclass
class FeatureOrder:
    """
    Attributes:
        id (Union[UUID, str]): The unique identifier of the item within the order.
        type (Union[Literal['Feature'], Unset]):  Default: 'Feature'.
        geometry (Union['PointGeometry', 'PolygonGeometry', None, Unset]): Defines the full footprint of the asset
            represented by the item.
        properties (Union['Order', None, Unset]): A dictionary of additional metadata for the item.
    """

    id: Union[UUID, str]
    type: Union[Literal["Feature"], Unset] = "Feature"
    geometry: Union["PointGeometry", "PolygonGeometry", None, Unset] = UNSET
    properties: Union["Order", None, Unset] = UNSET

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "id",
        }
