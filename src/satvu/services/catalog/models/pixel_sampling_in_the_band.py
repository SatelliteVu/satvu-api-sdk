from enum import Enum


class PixelSamplingInTheBand(str, Enum):
    AREA = "area"
    POINT = "point"

    def __str__(self) -> str:
        return str(self.value)
