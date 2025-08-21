from enum import Enum


class GeoJSONPolygon1Type(str, Enum):
    POLYGON = "Polygon"

    def __str__(self) -> str:
        return str(self.value)
