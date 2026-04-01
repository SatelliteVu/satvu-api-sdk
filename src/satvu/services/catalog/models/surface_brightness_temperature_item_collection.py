from enum import Enum


class SurfaceBrightnessTemperatureItemCollection(str, Enum):
    SURFACE_BRIGHTNESS_TEMPERATURE = "surface-brightness-temperature"

    def __str__(self) -> str:
        return str(self.value)
