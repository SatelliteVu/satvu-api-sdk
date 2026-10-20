from enum import StrEnum


class PixelSamplingInTheBand(StrEnum):
    AREA = "area"
    POINT = "point"

    def __str__(self) -> str:
        return str(self.value)
