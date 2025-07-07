from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, Union

if TYPE_CHECKING:
    from ..models.line_string import LineString
    from ..models.multi_line_string import MultiLineString
    from ..models.multi_point import MultiPoint
    from ..models.multi_polygon import MultiPolygon
    from ..models.point import Point
    from ..models.polygon import Polygon


@dataclass
class GeometryCollection:
    """GeometryCollection Model

    Attributes:
        type (Literal['GeometryCollection']):
        geometries (list[Union['GeometryCollection', 'LineString', 'MultiLineString', 'MultiPoint', 'MultiPolygon',
            'Point', 'Polygon']]):
        bbox (Union[None, list[float]]):
    """

    type: Literal["GeometryCollection"]
    geometries: list[
        Union[
            "GeometryCollection",
            "LineString",
            "MultiLineString",
            "MultiPoint",
            "MultiPolygon",
            "Point",
            "Polygon",
        ]
    ]
    bbox: Union[None, list[float]] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "type",
            "geometries",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "type": object,
            "geometries": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "bbox": object,
        }
