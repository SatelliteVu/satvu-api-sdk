from enum import Enum


class AssetRasterBandsPixelSamplingInTheBand(str, Enum):
    AREA = "area"
    POINT = "point"

    def __str__(self) -> str:
        return str(self.value)
