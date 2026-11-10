from enum import StrEnum


class Collection(StrEnum):
    PRIMARY = "primary"
    SURFACE_BRIGHTNESS_TEMPERATURE = "surface-brightness-temperature"

    def __str__(self) -> str:
        return str(self.value)
