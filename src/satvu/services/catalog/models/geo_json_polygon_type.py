from enum import StrEnum


class GeoJSONPolygonType(StrEnum):
    POLYGON = "Polygon"

    def __str__(self) -> str:
        return str(self.value)
