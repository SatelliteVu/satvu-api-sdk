from enum import StrEnum


class PrimaryFeatureCollectionType(StrEnum):
    FEATURECOLLECTION = "FeatureCollection"

    def __str__(self) -> str:
        return str(self.value)
