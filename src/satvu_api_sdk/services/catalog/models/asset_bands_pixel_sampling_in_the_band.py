from enum import Enum


class AssetBandsPixelSamplingInTheBand(str, Enum):
    AREA = "area"
    POINT = "point"

    def __str__(self) -> str:
        return str(self.value)
