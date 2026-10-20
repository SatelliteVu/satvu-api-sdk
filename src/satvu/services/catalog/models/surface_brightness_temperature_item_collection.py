from enum import StrEnum


class SurfaceBrightnessTemperatureItemCollection(StrEnum):
    SURFACE_BRIGHTNESS_TEMPERATURE = "surface-brightness-temperature"

    def __str__(self) -> str:
        return str(self.value)
