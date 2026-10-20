from enum import StrEnum


class GeoJSONMultiPolygonType(StrEnum):
    MULTIPOLYGON = "MultiPolygon"

    def __str__(self) -> str:
        return str(self.value)
