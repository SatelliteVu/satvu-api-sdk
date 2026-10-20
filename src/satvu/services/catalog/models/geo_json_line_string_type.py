from enum import StrEnum


class GeoJSONLineStringType(StrEnum):
    LINESTRING = "LineString"

    def __str__(self) -> str:
        return str(self.value)
