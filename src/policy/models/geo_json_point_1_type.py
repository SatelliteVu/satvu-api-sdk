from enum import Enum


class GeoJSONPoint1Type(str, Enum):
    POINT = "Point"

    def __str__(self) -> str:
        return str(self.value)
