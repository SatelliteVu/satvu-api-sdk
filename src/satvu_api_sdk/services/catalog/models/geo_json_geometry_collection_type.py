from enum import Enum


class GeoJSONGeometryCollectionType(str, Enum):
    GEOMETRYCOLLECTION = "GeometryCollection"

    def __str__(self) -> str:
        return str(self.value)
