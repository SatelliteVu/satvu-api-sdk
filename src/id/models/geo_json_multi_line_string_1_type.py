from enum import Enum


class GeoJSONMultiLineString1Type(str, Enum):
    MULTILINESTRING = "MultiLineString"

    def __str__(self) -> str:
        return str(self.value)
