from enum import StrEnum


class GeoJSONGeometryCollectionType(StrEnum):
    GEOMETRYCOLLECTION = "GeometryCollection"

    def __str__(self) -> str:
        return str(self.value)
