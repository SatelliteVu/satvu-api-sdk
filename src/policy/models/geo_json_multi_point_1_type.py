from enum import Enum


class GeoJSONMultiPoint1Type(str, Enum):
    MULTIPOINT = "MultiPoint"

    def __str__(self) -> str:
        return str(self.value)
