from enum import Enum


class GeoJSONGeometryCollection1Type(str, Enum):
    GEOMETRYCOLLECTION = "GeometryCollection"

    def __str__(self) -> str:
        return str(self.value)
