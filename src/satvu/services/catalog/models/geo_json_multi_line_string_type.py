from enum import StrEnum


class GeoJSONMultiLineStringType(StrEnum):
    MULTILINESTRING = "MultiLineString"

    def __str__(self) -> str:
        return str(self.value)
