from enum import StrEnum


class SurfaceBrightnessTemperatureFeatureCollectionType(StrEnum):
    FEATURECOLLECTION = "FeatureCollection"

    def __str__(self) -> str:
        return str(self.value)
