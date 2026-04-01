from enum import Enum


class AcquisitionFeatureCollectionType(str, Enum):
    FEATURECOLLECTION = "FeatureCollection"

    def __str__(self) -> str:
        return str(self.value)
