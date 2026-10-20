from enum import StrEnum


class GeoJSONPointType(StrEnum):
    POINT = "Point"

    def __str__(self) -> str:
        return str(self.value)
