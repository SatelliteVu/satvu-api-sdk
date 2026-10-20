from enum import StrEnum


class SurfaceBrightnessTemperatureItemType(StrEnum):
    FEATURE = "Feature"

    def __str__(self) -> str:
        return str(self.value)
