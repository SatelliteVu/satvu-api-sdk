from enum import Enum


class SurfaceBrightnessTemperatureFeatureCollectionType(str, Enum):
    FEATURECOLLECTION = "FeatureCollection"

    def __str__(self) -> str:
        return str(self.value)
