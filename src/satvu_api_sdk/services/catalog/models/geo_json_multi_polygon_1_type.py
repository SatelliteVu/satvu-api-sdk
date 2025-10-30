from enum import Enum


class GeoJSONMultiPolygon1Type(str, Enum):
    MULTIPOLYGON = "MultiPolygon"

    def __str__(self) -> str:
        return str(self.value)
