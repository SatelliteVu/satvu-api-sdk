from enum import StrEnum


class AcquisitionFeatureCollectionType(StrEnum):
    FEATURECOLLECTION = "FeatureCollection"

    def __str__(self) -> str:
        return str(self.value)
