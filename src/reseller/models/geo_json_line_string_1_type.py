from enum import Enum


class GeoJSONLineString1Type(str, Enum):
    LINESTRING = "LineString"

    def __str__(self) -> str:
        return str(self.value)
