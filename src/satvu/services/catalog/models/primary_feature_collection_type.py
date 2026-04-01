from enum import Enum


class PrimaryFeatureCollectionType(str, Enum):
    FEATURECOLLECTION = "FeatureCollection"

    def __str__(self) -> str:
        return str(self.value)
