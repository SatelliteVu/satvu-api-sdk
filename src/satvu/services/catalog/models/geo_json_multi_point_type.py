from enum import StrEnum


class GeoJSONMultiPointType(StrEnum):
    MULTIPOINT = "MultiPoint"

    def __str__(self) -> str:
        return str(self.value)
